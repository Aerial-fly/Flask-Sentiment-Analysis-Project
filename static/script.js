// Menunggu hingga seluruh halaman HTML dimuat
document.addEventListener('DOMContentLoaded', () => {
    // Ambil elemen-elemen dari HTML
    const predictBtn = document.getElementById('predict-btn');
    const textInput = document.getElementById('text-input');
    const resultContainer = document.getElementById('result-container');

    // Tambahkan 'event listener' saat tombol diklik
    predictBtn.addEventListener('click', () => {
        const inputText = textInput.value;

        if (!inputText) {
            alert("Harap masukkan teks terlebih dahulu!");
            return;
        }

        resultContainer.innerHTML = "Menganalisis...";

        // Mengirim data ke API Flask kita menggunakan Fetch API
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ teks: inputText }),
        })
        .then(response => response.json()) // Mengubah respons menjadi JSON
        .then(data => {
            // Menampilkan hasil dari API ke halaman web
            if (data.sentimen === 'positif') {
                resultContainer.innerHTML = `<p style="color: green;">Sentimen: Positif 😊</p>`;
            } else {
                resultContainer.innerHTML = `<p style="color: red;">Sentimen: Negatif 😠</p>`;
            }
        })
        .catch((error) => {
            // Menampilkan error jika API tidak bisa diakses
            console.error('Error:', error);
            resultContainer.innerHTML = `<p style="color: orange;">Gagal terhubung ke server.</p>`;
        });
    });
});