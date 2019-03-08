let spinner = document.querySelector('.spinner');
let content = document.querySelector('.content');
let footer = document.querySelector('footer');

content.style.overflow = 'hidden';
content.style.position = 'fixed';

window.addEventListener('load', e => {
  content.style.visibility = 'visible';
  footer.style.visibility = 'visible';
  content.style.position = 'static';
  spinner.style.display = 'none';
});
