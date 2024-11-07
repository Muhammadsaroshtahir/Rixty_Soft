function myFunction() {
    const x = document.getElementById("alphabets").value;
    let text;
    
    const regex = /^[a-z]+$/;

    if (regex.test(x)) {
        text = "Input OK";
    } else {
        text = "Input not valid. Please enter only lowercase letters (a-z).";
    }

    document.getElementById("demo").innerHTML = text;
}
