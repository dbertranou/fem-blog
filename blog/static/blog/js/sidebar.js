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
