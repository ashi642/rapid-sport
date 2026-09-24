from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render
)

from .forms import OrderForm, CustomJerseyForm
from .models import Product, Order, CustomJersey


def home(request):

    featured_products = Product.objects.filter(
        is_featured=True,
        stock__gt=0
    )[:8]

    categories = [
        "Football",
        "Cricket",
        "Custom",
        "Accessories",
    ]

    return render(
        request,
        "shop/home.html",
        {
            "featured_products": featured_products,
            "categories": categories,
        }
    )


def shop(request):

    category = request.GET.get("category")

    products = Product.objects.all()

    if category:
        products = products.filter(category=category)

    categories = Product.CATEGORY_CHOICES

    return render(
        request,
        "shop/shop.html",
        {
            "products": products,
            "categories": categories,
            "selected_category": category,
        }
    )


def product_detail(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    return render(
        request,
        "shop/product.html",
        {
            "product": product
        }
    )


def custom_jersey(request):

    if request.method == "POST":

        form = CustomJerseyForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Your custom jersey request has been submitted!"
            )

            return redirect("custom_jersey")

    else:
        form = CustomJerseyForm()

    return render(
        request,
        "shop/custom.html",
        {
            "form": form
        }
    )


def add_to_cart(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    if product.stock <= 0:

        messages.error(
            request,
            "This product is currently out of stock."
        )

        return redirect("product_detail", id=id)

    cart = request.session.get("cart", {})

    product_id = str(product.id)

    if product_id in cart:

        if cart[product_id]["quantity"] < product.stock:
            cart[product_id]["quantity"] += 1

    else:

        cart[product_id] = {
            "quantity": 1,
            "size": product.size.split(",")[0].strip()
            if product.size else ""
        }

    request.session["cart"] = cart
    request.session.modified = True

    messages.success(
        request,
        f"{product.name} added to cart."
    )

    return redirect("cart")


def remove_from_cart(request, id):

    cart = request.session.get("cart", {})

    product_id = str(id)

    if product_id in cart:
        del cart[product_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


def update_cart(request):

    if request.method == "POST":

        cart = request.session.get("cart", {})

        for product_id, item in cart.items():

            quantity = request.POST.get(
                f"quantity_{product_id}"
            )

            size = request.POST.get(
                f"size_{product_id}"
            )

            if quantity:

                try:
                    quantity = int(quantity)

                    product = Product.objects.get(
                        id=product_id
                    )

                    quantity = max(
                        1,
                        min(quantity, product.stock)
                    )

                    item["quantity"] = quantity

                except (
                    ValueError,
                    Product.DoesNotExist
                ):
                    pass

            if size:
                item["size"] = size

        request.session["cart"] = cart
        request.session.modified = True

    return redirect("cart")


def cart(request):

    cart_data = request.session.get(
        "cart",
        {}
    )

    cart_items = []

    total = 0

    for product_id, item in cart_data.items():

        try:

            product = Product.objects.get(
                id=product_id
            )

            quantity = item["quantity"]

            item_total = product.price * quantity

            total += item_total

            cart_items.append({
                "product": product,
                "quantity": quantity,
                "size": item.get("size", ""),
                "item_total": item_total,
            })

        except Product.DoesNotExist:
            continue

    order_form = OrderForm()

    return render(
        request,
        "shop/cart.html",
        {
            "cart_items": cart_items,
            "total": total,
            "order_form": order_form,
        }
    )


def checkout(request):

    cart_data = request.session.get(
        "cart",
        {}
    )

    if not cart_data:

        messages.error(
            request,
            "Your cart is empty."
        )

        return redirect("shop")


    first_item = next(
        iter(cart_data.items())
    )

    product_id = first_item[0]

    item = first_item[1]

    product = get_object_or_404(
        Product,
        id=product_id
    )


    if request.method == "POST":

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)

            order.product = product

            order.size = item.get(
                "size",
                ""
            )

            order.quantity = item.get(
                "quantity",
                1
            )

            order.save()

            request.session["cart"] = {}

            messages.success(
                request,
                "Order placed successfully!"
            )

            return redirect(
                "order_success",
                id=order.id
            )

    else:

        form = OrderForm()

    return render(
        request,
        "shop/cart.html",
        {
            "cart_items": build_cart_items(request),
            "total": calculate_cart_total(request),
            "order_form": form,
        }
    )


def build_cart_items(request):

    cart_data = request.session.get(
        "cart",
        {}
    )

    items = []

    for product_id, item in cart_data.items():

        try:

            product = Product.objects.get(
                id=product_id
            )

            quantity = item["quantity"]

            items.append({
                "product": product,
                "quantity": quantity,
                "size": item.get("size", ""),
                "item_total": product.price * quantity,
            })

        except Product.DoesNotExist:
            pass

    return items


def calculate_cart_total(request):

    total = 0

    for item in build_cart_items(request):
        total += item["item_total"]

    return total


def order_success(request, id):

    order = get_object_or_404(
        Order,
        id=id
    )

    return render(
        request,
        "shop/order_success.html",
        {
            "order": order
        }
    )


def dashboard_login(request):

    if request.user.is_authenticated:

        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "shop/dashboard_login.html"
    )


@login_required
def dashboard(request):

    orders = Order.objects.select_related(
        "product"
    ).all()

    custom_orders = CustomJersey.objects.all()

    total_orders = orders.count()

    pending_orders = orders.filter(
        status="Pending"
    ).count()

    shipped_orders = orders.filter(
        status="Shipped"
    ).count()

    delivered_orders = orders.filter(
        status="Delivered"
    ).count()

    total_sales = sum(
        order.total_price
        for order in orders
        if order.status == "Delivered"
    )

    return render(
        request,
        "shop/dashboard.html",
        {
            "orders": orders,
            "custom_orders": custom_orders,
            "total_orders": total_orders,
            "pending_orders": pending_orders,
            "shipped_orders": shipped_orders,
            "delivered_orders": delivered_orders,
            "total_sales": total_sales,
        }
    )


@login_required
def dashboard_logout(request):

    logout(request)

    return redirect("home")