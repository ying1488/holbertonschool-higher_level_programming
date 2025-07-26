#!/usr/bin/node

const ul = document.querySelector('.my_list');
const newItem = document.createElement('li');

document.addEventListener('DOMContentLoaded', function () {
  newItem.textContent = "Item";
  ul.appendChild(newItem);
});
