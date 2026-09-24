function toggleMenu() {

    const menu = document.getElementById("mobileMenu");

    if (menu) {
        menu.classList.toggle("hidden");
    }
}


setTimeout(() => {

    const messages = document.querySelectorAll(
        '[class*="bg-yellow-400"]'
    );

    messages.forEach(message => {

        if (
            message.textContent.includes("added") ||
            message.textContent.includes("successfully")
        ) {

            setTimeout(() => {

                message.style.transition = "opacity 0.5s";
                message.style.opacity = "0";

            }, 3500);

        }

    });

}, 100);