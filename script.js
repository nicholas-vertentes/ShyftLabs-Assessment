curPage = 'HomePage';

function loadPage(pageName) {
  // Make an AJAX request to fetch the content of the selected page
  fetch(`${pageName}.html`)
      .then(response => response.text())
      .then(data => {
          document.getElementById('content').innerHTML = data;
      })
      .catch(error => console.error('Error loading page:', error));
}

// Initial load (e.g., Home page)
window.onload = function () {
  loadPage(curPage);
};