document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll(".drop-zone__input").forEach(inputElement => {
        
        const dropZoneElement = inputElement.closest(".drop-zone");

        dropZoneElement.addEventListener("click", e=> {
            inputElement.click();
        });
        
        dropZoneElement.addEventListener("dragover", e => {
            e.preventDefault();
            dropZoneElement.classList.add("drop-zone--over");
        });

        ["dragleave", "dragend"].forEach(type => {
            dropZoneElement.addEventListener(type, e => {
                dropZoneElement.classList.remove('drop-zone--over');
            });
        });

        dropZoneElement.addEventListener("drop", e=> {
            e.preventDefault();
            console.log(e);

            if(e.dataTransfer.files.length) {
                inputElement.files = e.dataTransfer.files;
                updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
            }

            dropZoneElement.classList.remove("drop-zone--over");
        });

        inputElement.addEventListener("change", e =>{
            if (inputElement.files.length) {
                updateThumbnail(dropZoneElement, inputElement.files[0]);
            }
        });
    });
}, false);

function updateThumbnail(dropZoneElement, file) {
    let thumnailElement = dropZoneElement.querySelector(".drop-zone__thumb");

    if(dropZoneElement.querySelector(".drop-zone__prompt")) {
        dropZoneElement.querySelector(".drop-zone__prompt").remove();
    }

    if(!thumnailElement) {
        thumnailElement = document.createElement("div");
        thumnailElement.classList.add("drop-zone__thumb");
        dropZoneElement.appendChild(thumnailElement);
    }

    thumnailElement.dataset.label = file.name;

    if(file.type.startsWith("image/")) {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            thumnailElement.style.backgroundImage = `url('${reader.result}')`;
        };
    }
}