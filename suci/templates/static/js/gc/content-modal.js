const modal = document.getElementById('modal');
const btnClose = document.getElementsByClassName('close')[0];

const socialMediaAccountAdd = document.querySelector('[data-gc-sma-add]');
socialMediaAccountAdd.onclick = function (event) {
  event.preventDefault();

  const title = document.querySelector('[data-modal-header-title]');
  title.textContent = 'Registrar una Red Social';

  const form = document.querySelector('[data-gc-form]');
  form.method = 'POST'
  form.action = "social-media-account";

  modal.style.display = 'block';
  modal.style.visibility = "visible";
  modal.style.opacity = 1;
};

document.querySelectorAll('.btn-update').forEach(function (btn) {
  btn.onclick = function (event) {
    event.preventDefault();
    const socialMediaId = btn.getAttribute('data-gc-sma-id');
    const form = document.getElementById('form');
    form.method = 'PUT'
    form.action = "social-media-account/actualizar/" + socialMediaId;

    const socialMedia = btn.getAttribute('data-gc-sma');
    document.getElementById('gc-sma-platform').value = socialMedia.platform;
    document.getElementById('gc-sma-username').value = socialMedia.username;
    document.getElementById('gc-sma-url').value = socialMedia.url;
    document.getElementById('gc-sma-followers').value = socialMedia.followers;
    document.getElementById('gc-sma-responsible').value = socialMedia.responsible;
    document.getElementById('gc-sma-publications').value = socialMedia.publications;

    modal.style.display = 'block';
    modal.style.visibility = "visible";
    modal.style.opacity = 1;
  };
});
