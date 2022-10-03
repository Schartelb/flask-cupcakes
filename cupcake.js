$('.add-cupcake').click(addCupcake)

async function addCupcake() {
    infocake = document.getElementsByClassName('info')
    addcake = {}
    for (info of infocake) {
        addcake[info.name] = info.value
    }
    await axios.post("/api/cupcakes", addcake)
    document.getElementById("cupcakes").contentWindow.location.reload(true);
}