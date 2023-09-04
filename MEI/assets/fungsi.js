// HITUNG MUNDUR WAKTU HAFLAH by: Nu'man Nasyar MZ
// instagram: @numen_18
const countDownDate = new Date("December 18, 2023 00:00:00").getTime(); //seting tanggal mulainya

const x = setInterval(function () {
  // update waktunya tiap detik
  const now = new Date().getTime(); // pake tanggal terbaru
  const distance = countDownDate - now; // cari selisih tanggal sekarang dan tanggal haflah
  const days = Math.floor(distance / (1000 * 60 * 60 * 24)); // hitungan hari, jam, menit, detik
  const hours = Math.floor(
    (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
  );
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);
  const countdownTimer = `${days} HARI, ${hours
    .toString()
    .padStart(2, "0")} JAM, ${minutes
    .toString()
    .padStart(2, "0")} MENIT, ${seconds.toString().padStart(2, "0")} DETIK`; // format waktunya di html: hari, jam, menit, detik
  document.getElementById("countdown").innerHTML = countdownTimer;
  if (distance < 0) {
    // kalo waktunya habis gimana?
    clearInterval(x);
    document.getElementById("countdown").innerHTML = "Sedang Berlangsung!";
  }
}, 1000);
