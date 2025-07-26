#!/usr/bin/node

window.onload = () => {
  let hello = document.getElementById('hello');

  fetch ("https://hellosalut.stefanbohacek.com/?lang=fr")
    .then((response) => {
        if (!response.ok) {
            throw new Error (`HTTP error: ${response.status}`);
        }
        return response.json();
    })
    .then ((json)=>{
        hello.textContent = json.hello;
    })
    .catch ((err) => console.error(`Fetch problem: ${err.message}`));
}