function prepare (title, message, date) {
  const toastHtml = document.getElementById('toast')
  document.getElementById('toast-title').textContent = title
  document.getElementById('toast-date').textContent = date
  document.getElementById('toast-message').textContent = message
  const toast = new bootstrap.Toast(toastHtml)
  toast.show()
}

function toast (title, message, date = 'Hace un momento') {
  prepare(title, message, date)
}

function toastSecondary (title, message, date = 'Hace un momento') {
  $('#toast').removeClass('bg-primary').addClass(`bg-secondary`)
  prepare(title, message, date)
}

function toastInfo (title, message, date = 'Hace un momento') {
  $('#toast').removeClass('bg-primary').addClass(`bg-info`)
  prepare(title, message, date)
}

function toastSuccess (title, message, date = 'Hace un momento') {
  $('#toast').removeClass('bg-primary').addClass(`bg-success`)
  prepare(title, message, date)
}

function toastWarning (title, message, date = 'Hace un momento') {
  $('#toast').removeClass('bg-primary').addClass(`bg-warning`)
  prepare(title, message, date)
}

function toastError (title, message, date = 'Hace un momento') {
  $('#toast').removeClass('bg-primary').addClass(`bg-danger`)
  prepare(title, message, date)
}