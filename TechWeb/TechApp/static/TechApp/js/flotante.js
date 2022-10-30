const btnOpenS =
document.querySelector("#btn-open-modalS");
const btnCerrarS =
document.querySelector("#btn-cerrar-modalS");
const modal =
document.querySelector("#modalS");

btnOpenS.addEventListener("click",()=>{
        modalS.showModal();
})
btnCerrarModalS.addEventListener("click",()=>{
    modalS.close()
})