var modal = document.getElementById("photoModal");
var obj;

function displayModal(param) {
    let performance = param.getAttribute("data-performance");
    let year = param.getAttribute("data-year");
    let guild = param.getAttribute("data-guild");
    let image = param.getAttribute("data-image");
    let costume = param.getAttribute("data-costume");
    let character = param.getAttribute("data-character");
    let author = param.getAttribute("data-author");
    let model = param.getAttribute("data-model");
    let apertureValue = param.getAttribute("data-apertureValue");
    let exposureTime = param.getAttribute("data-exposureTime");
    let focalLength = param.getAttribute("data-focalLength");
    let id = param.getAttribute("data-id");
    if(!modal){
        modal = document.getElementById("photoModal");
    }
    document.getElementById("imageModal").src="/media/" + image;
    updateText("performanceModal", performance);
    updateText("yearModal", year);
    updateText("guildModal", guild);
    updateText("costumeModal", costume);
    updateText("characterModal", character);
    updateText("authorModal", author);
    updateText("model", model);
    updateText("apertureValue", apertureValue);
    updateText("exposureTime", exposureTime);
    updateText("focalLength", focalLength);
    document.getElementById("postId").value = id;
    modal.style.display = "block";
}

function updateText(id, newText) {
    let ele = document.getElementById(id);
    ele.innerHTML = newText;
}

window.onclick = function(event) {
    if(!modal) {
        modal = document.getElementById("photoModal");
    }
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function closeModal() {
    document.getElementById("imageModal").src="";
    modal.style.display = "none";
}

function downloadPdf() {
    let id = document.getElementById("postId").value;
    console.log(id);
    window.open("/pdf/" + id, "_blank");
}



