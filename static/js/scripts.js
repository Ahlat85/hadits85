$(document).ready(function() {
  $(".btn-wait").on("click", () => {
    swal("Mohon tunggu, sedang memproses!");
  });
  $(".btn-refresh").on("click", () => {
    location.reload(true);
  });
  $(".btn-copy-link").on("click", () => {
    swal({
      title: "Menyalin URL",
      text: "Apakah Anda Hendak Menyalin URL?",
      icon: "warning",
      buttons: [
        "Tidak, batalkan!",
        "Iya, salin!"
      ]
    }).then(function(isConfirm) {
      if (isConfirm) {
        const url = window.location.href;
        navigator.clipboard.writeText(url);
        swal("Berhasil Salin URL!", `Jika browser tidak mendukung bisa lakukan secara manual dengaan URL: ${url}`, "success");
      }
    })
  });
});