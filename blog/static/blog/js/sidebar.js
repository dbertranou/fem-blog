// toggle sidebar
let sidebar = document.querySelector('.sidebar');
let openBtn = document.querySelector('#open-sidebar-btn');
let closeBtn = document.querySelector('#close-sidebar-btn');
let sidebarIsOpen = false;

const openSidebar = () => {
  sidebar.style.right = 0;
  sidebarIsOpen = true;
  document.body.style.overflowY = 'hidden';
}

const closeSidebar = () => {
  sidebar.style.right = '-800px';
  sidebarIsOpen = false;
  document.body.style.overflowY = 'visible';
}

openBtn.addEventListener('click', e => {
  openSidebar();
  sidebarIsOpen = true;
});

closeBtn.addEventListener('click', e => {
  closeSidebar();
  sidebarIsOpen = false;
});

// populate sidebar categories and tags
let sidebarCategories = document.querySelector('.sidebar-categories');
let sidebarTags = document.querySelector('.sidebar-tags');

fetch('/api/filters')
  .then(response => response.json())
  .then(json => {
    json.categories.map(item => {
      a = document.createElement('a');
      a.setAttribute('href', item.url);
      a.innerText = item.name;
      li = document.createElement('li');
      li.appendChild(a);
      sidebarCategories.appendChild(li)
    });
    json.tags.map(item => {
      li = document.createElement('li');
      li.innerText = item.readable_name;
      sidebarTags.appendChild(li)
    });
  });
