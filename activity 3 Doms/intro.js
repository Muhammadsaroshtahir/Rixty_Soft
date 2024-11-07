function changetext() {

    document.getElementById("text").innerHTML="the text has been changed!"
}

function changestyle(){

    const paragraph = document.getElementById("text");
    paragraph.style.color="red";
    paragraph.style.fontSize= "25px"
}