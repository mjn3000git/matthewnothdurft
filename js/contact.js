// matthewnothdurft.com contact form (Formspree, free plan), same setup as Adirondack Craftworks js/inquiry.js.
// To turn the form on, paste the Formspree form ID (the part after formspree.io/f/) between the quotes below.
// While it is empty, the form still shows, but nothing is posted; Send shows a short note instead.
const FORMSPREE_ID = "xaeeebnq";

(function () {
  var form = document.getElementById("contact-form");
  if (!form) return;
  var note = document.getElementById("contact-form-note");
  var id = (FORMSPREE_ID || "").trim();
  if (/^[A-Za-z0-9]+$/.test(id)) {
    form.setAttribute("action", "https://formspree.io/f/" + encodeURIComponent(id));
    form.setAttribute("method", "POST");
    return;
  }
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (note) {
      note.textContent = "Thanks for writing. This form isn't connected yet, so your note wasn't sent. Please call 518-832-9174 for now.";
      note.hidden = false;
    }
  });
})();
