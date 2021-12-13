
var modal = document.getElementById("photoModal");


function displayModal(param) {
    let performance = param.getAttribute("data-performance");
    let year = param.getAttribute("data-year");
    let guild = param.getAttribute("data-guild")
    let image = param.getAttribute("data-image")
    let costume = param.getAttribute("data-costume")
    let character = param.getAttribute("data-character")
    let author = param.getAttribute("data-author")
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
    modal.style.display = "none";
}