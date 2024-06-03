const modal = document.getElementById('modal');
const btnClose = document.getElementsByClassName('close')[0];
const btnAdd = document.querySelector('[data-btn-add]');

document.addEventListener('DOMContentLoaded', function () {
  btnClose.onclick = function () {
    modal.style.visibility = "hidden";
    modal.style.opacity = 0;
    modal.style.display = 'none';
  };

  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.visibility = "hidden";
      modal.style.opacity = 0;
      modal.style.display = 'none';
    }
  };
});

const modalHeaderTitle = (textContent) => {
  const title = document.querySelector('[data-modal-header-title]');
  title.textContent = textContent;
}

const modalConfigForm = ({ method, action }) => {
  const form = document.querySelector('[data-form]');
  form.method = method;
  form.action = action;
}

const openModal = () => {
  modal.style.display = 'block';
  modal.style.visibility = "visible";
  modal.style.opacity = 1;
}

const showForm = ({ textContent, method, action }) => {
  btnAdd.onclick = (event) => {
    event.preventDefault();

    modalHeaderTitle(textContent);
    modalConfigForm(method, action);
    openModal();
  };
}

const postForm = ({ textContent, action }) => {
  showForm({ textContent, method: 'POST', action });
}

const putForm = ({ textContent, action }) => {
  showForm({ textContent, method: 'PUT', action });
}

export {
  showForm,
  postForm,
  putForm
}