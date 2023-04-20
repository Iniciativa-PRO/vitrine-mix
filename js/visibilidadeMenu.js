// Alterar a visibilidade do menu, quando é clicado o ícone do menu
function visibilidadeMenu() {
    let menuMobile = document.querySelector(".menu-mobile");

    menuMobile.addEventListener("click", () => {

        let menuContener = document.querySelector(".menu__contener");
        let verificarClassExistente = menuContener.classList.toggle("menu__contener--display");

        if (verificarClassExistente == true) {

            let menuContenerDisplay = document.querySelector(".menu__contener--display");
            menuContenerDisplay.style.display = "block";

        } else {

            menuContener.style.display = "none";
        }
    })
}
visibilidadeMenu();