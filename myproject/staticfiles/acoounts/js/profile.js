function profilAdd() {
    return `
    <title>Profil Sayfası</title>

    <div class="profil-backgraund">
        
        <div class="container-profil">
            <img src="img/images.png" alt="Profil Resmi" class="profile-img">
            <div class="profile-info">
                <p><strong>Ad Soyad:</strong> <span id="fullName"></span></p>
                <p><strong>Kullanıcı Adı:</strong> <span id="username"></span></p>
                <p><strong>E-Posta:</strong> <span id="email"></span></p>
            </div>
        </div>
        
        <script>
            // Profil bilgileri
            const profil = {
                fullName: "muhammetalidurmus@gmail.com",
                kullaniciAdi: "kullanici123",
                eposta: "ornek@eposta.com"
            };
        
        
            // Profil bilgilerini güncelle
            document.getElementById("fullName").textContent = fullName;
            document.getElementById("username").textContent = profil.kullaniciAdi;
            document.getElementById("email").textContent = profil.eposta;
        </script>
        
        <div id="back-button-container"onclick="changePage('home')">
        <button id="back-button">Back</button>
        </div>

    </div>
    `;
}


