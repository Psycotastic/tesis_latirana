function accordionBackup(param) {
    param.classList.toggle("active");
    var panel = param.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    } 
}