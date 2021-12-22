var modal = document.getElementById("photoModal");
var obj;

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
    //getEXIF();
    //let metadata = document.getElementById("metadataJson").value;
    //console.log(metadata);
    /*if(metadata != "") {
        const jsonObj = JSON.parse(metadata);
        console.log(jsonObj);
        let apertureValue = jsonObj.ApertureValue;
        let focalLength = jsonObj.FocalLength;
        let exposureTime = jsonObj.ExposureTime;
        let iso = jsonObj.ISOSpeedRatings;
        let flash = jsonObj.Flash;
    }*/
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
    document.getElementById("metadataJson").value = "";
}

function getEXIF(e) {
    try {
        console.log(e);
        console.log("AAAAAA");
        let test = new EXIF();
        test.getData(e, function() {
            obj = EXIF.getAllTags(e);
            let json = JSON.stringify(obj, null, "\t");
            //document.getElementById("metadataJson").value = json;
            console.log(json);
        });
    }catch(err) {
        console.log(err);
        //document.getElementById("metadataJson").value = "";
    }
}

