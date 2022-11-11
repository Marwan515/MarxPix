function chang() {
    let checkval = document.getElementById("cngval");
    if (checkval.value == "1") {
        document.getElementById("dat").disabled = false;
        document.getElementById("sol").disabled = true;
    } else if (checkval.value == "2") {
        document.getElementById("sol").disabled = false;
        document.getElementById("dat").disabled = true; 
    } else {
        document.getElementById("dat").disabled = true;
        document.getElementById("sol").disabled = true;
    }
}