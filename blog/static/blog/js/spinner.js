let spinner = document.querySelector('.spinner');
let content = document.querySelector('.content');

content.style.overflow = 'hidden';
content.style.position = 'fixed';

window.addEventListener('load', e => {
  content.style.visibility = 'visible';
  content.style.position = 'static';
  spinner.style.display = 'none';
});
