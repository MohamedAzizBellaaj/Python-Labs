function UpperLowerAlternator(val) {
  const p = document.querySelector("p");
  for (let i = 0; i < val.length; i++) {
    if (val[i] == " ") {
      continue;
    }
    if (i % 2 == 1)
      val =
        val.substring(0, i) +
        val.charAt(i).toUpperCase() +
        val.substring(i + 1);
  }
  p.innerText = val;
  console.log(val)
}
