const btnClose = document.querySelector("#close-btn");
const messageBox = document.querySelector("#message-container");

btnClose.addEventListener("click", () => {
    messageBox.classList.add("d-none");
    console.log("Clicked!")
})
