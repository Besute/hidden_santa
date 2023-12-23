var script = document.createElement("script");
script.src = "https://code.jquery.com/jquery-3.6.3.min.js"; // Check https://jquery.com/ for the current version
document.getElementsByTagName("head")[0].appendChild(script);
const section2 = document.querySelector(".section--2");
const buttonSection2 = document.querySelector(".header-text-1");
const buttons = document.querySelectorAll(".button--inside");
const buttonCont = document.querySelectorAll(".buttonText");
const button1 = document.querySelector(".button");
const button2 = document.querySelector(".button2");
const frnds = document.querySelector(".join-friends");
const section3 = document.querySelector(".section--3");

buttonSection2.addEventListener("click", (e) => {
  e.preventDefault();
  document
    .querySelector(".button--inside")
    .scrollIntoView({ behavior: "smooth" });
});

buttons.forEach((button) => {
  button.addEventListener("mousedown", (e) => {
    e.target.closest(".button--inside").classList.add("active");
  });
});
buttons.forEach((button) => {
  button.addEventListener("mouseup", (e) => {
    e.target.closest(".button--inside").classList.remove("active");
    section3.scrollIntoView({ behavior: "smooth" });
  });
});

function reg(event) {
  event.preventDefault();
  const regPassword = document.querySelector(".form--pass").value;
  const logEmail = document.querySelector(".form--email").value;
  const nameCap = document.querySelector(".form--name").value;
  document.querySelector(".form--pass").value =
    document.querySelector(".form--name").value =
    document.querySelector(".form--email").value =
      "";
  let capName = nameCap;
  let regPass = regPassword;
  let emailLog = logEmail;

  fetch(
    `http://89.223.123.82:5678/get?one=${capName}&two=${regPass}&three=${emailLog}`
  )
    .then((data) => {
      console.log(data);
      return data.json();
    })
    .catch((err) => {
      let errrr = err;
    })
    .then((data) => {
      console.log(data);
    });
}

document.querySelector(".register").addEventListener("submit", reg);

const form2 = document.querySelector(".form--2");

document.querySelector(".header-text-2").addEventListener("click", (e) => {
  e.preventDefault();
  section2.scrollIntoView({ behavior: "smooth" });
});
document.querySelector(".header-text-3").addEventListener("click", (e) => {
  e.preventDefault();
  frnds.scrollIntoView({ behavior: "smooth" });
});

document.querySelector(".form--2").addEventListener("submit", (e) => {
  e.preventDefault();
  const enteredPassword = document.querySelector(".form--pass--2").value;
  const emailReal = document.querySelector(".form--email--2").value;
  const nameUser = document.querySelector(".form--name--2").value;
  const enteredEmail = document.querySelector(".form--login--2").value;
  document.querySelector(".form--pass--2").value =
    document.querySelector(".form--name--2").value =
    document.querySelector(".form--email--2").value =
    document.querySelector(".form--login--2").value =
      "";
  let memName = nameUser;
  let login = enteredEmail;
  let pass = enteredPassword;
  let email = emailReal;
  fetch(
    `http://89.223.123.82:5678/get?one=${memName}&two=${login}&three=${email}&four=${pass}`
  )
    .then((data) => {
      console.log(data);
      return data.json();
    })
    .catch((err) => {
      let errrr = err;
    })
    .then((data) => {
      console.log(data);
    });
});

document.querySelector(".gameStarter").addEventListener("submit", (e) => {
  e.preventDefault();
  document.querySelector(".start-email").value = document.querySelector(
    ".start-pass"
  ).value = "";
});
document.querySelector(".gameStarter").addEventListener("submit", (e) => {
  e.preventDefault();
  let startEm = document.querySelector(".start-email").value;
  let pass = document.querySelector(".start-pass").value;
  fetch(`http://89.223.123.82:5678/get?one=${startEm}&two=${pass}`)
    .then((data) => {
      console.log(data);
      return data.json();
    })
    .catch((err) => {
      let errrr = err;
    })
    .then((data) => {
      console.log(data);
    });
});
