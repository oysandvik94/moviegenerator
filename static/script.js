function generateMovie() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var result = xhr.responseText;
            console.log(result)
            document.getElementById("title").innerHTML = result;
        }
    };
    xhr.open("GET", "/requestMovie", true);
    xhr.send(null);
}