let output = document.getElementById("outputLog")
setInterval(() => {
    fetch("http://127.0.0.1:8080/log-api")
    .then(response => response.json())
    .then(data => {
        if (data.length==0) {
            output.innerHTML=""
        }
        else{
            output.innerHTML += `<p>=>${data[data.length-1]}</p>`
            output.scrollTop = output.scrollHeight;
        }
    });

}, 100000);

document.addEventListener('loadstart',()=>{
  console.log("loading");
})