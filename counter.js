import countapi from 'countapi-js';

const counter = document.getElementById('counter')

countapi.visits().then((result => {
  counter.innerHTML = result.value;
}
