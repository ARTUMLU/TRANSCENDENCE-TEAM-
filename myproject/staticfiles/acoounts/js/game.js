function gameAdd() {
    return `
    <title> PONG GAME </title>

    <div class="profil-backgraund">
        <button class="start-button" onclick="changePage('pong-game')">
        <img src="img/basla.png" alt="buttonstart" style="width: 250px; height: 100px;"/>
        </button>

        <div id="back-button-container"onclick="changePage('home')">
        <button id="back-button">Back</button>
        </div>

    `;
}

function buttonstart() {
    return `
    <title> PONG GAME </title>

     <div class="profil-backgraund">
        <canvas id="pong" width="600" height="400"></canvas>
        <div id="back-button-container"onclick="changePage('home')">
        <button id="back-button">Back</button>
        </div>
    `;
}
