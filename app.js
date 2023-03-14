
let pass = document.getElementById("pass")
let cookie = document.getElementById("cookie")
let getCookie = document.getElementById("get-cookie")

getCookie.addEventListener("click", function() {
    cookie.value = pass.value;
})

function copyToClipboard() {
    var copyText = document.getElementById("cookie");
    copyText.select();
    document.execCommand("copy");
  
}