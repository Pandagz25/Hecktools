<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Python Hacking Tool v3.0 - EDU</title>
  <style>
    body {
      background-color: #0d0d0d;
      color: #00ff00;
      font-family: monospace;
      padding: 20px;
    }
    h1, h2 {
      color: #00ffff;
    }
    .codebox {
      background-color: #1a1a1a;
      border: 1px solid #333;
      padding: 10px;
      margin: 10px 0;
      position: relative;
    }
    .copy-btn {
      position: absolute;
      top: 5px;
      right: 10px;
      background: #333;
      color: #00ff00;
      border: none;
      padding: 4px 8px;
      cursor: pointer;
    }
    .copy-btn:hover {
      background: #555;
    }
  </style>
</head>
<body>

<h1>🐍 Python Hacking Tool v3.0</h1>
<p>Terminal-based tool untuk edukasi keamanan jaringan (INFOSEC).</p>
<p><strong>⚠️ Hanya untuk pembelajaran dan testing sistem milik sendiri.</strong></p>

<h2>📦 Cara Install (Termux)</h2>
<div class="codebox">
  <button class="copy-btn" onclick="copyCode(this)">Salin</button>
<pre><code>pkg update && pkg upgrade -y
pkg install python curl iputils -y
pip install requests beautifulsoup4 dnspython</code></pre>
</div>

<h2>▶️ Menjalankan Script</h2>
<div class="codebox">
  <button class="copy-btn" onclick="copyCode(this)">Salin</button>
<pre><code>python toolv3.py</code></pre>
</div>

<h2>📚 Kebutuhan Module</h2>
<div class="codebox">
  <button class="copy-btn" onclick="copyCode(this)">Salin</button>
<pre><code>pip install -r requirements.txt</code></pre>
</div>

<h3>📄 Isi file <code>requirements.txt</code></h3>
<div class="codebox">
  <button class="copy-btn" onclick="copyCode(this)">Salin</button>
<pre><code>requests
beautifulsoup4
dnspython</code></pre>
</div>

<h2>🛑 Disclaimer Hukum</h2>
<ul>
  <li>❌ Dilarang menggunakan tools ini untuk menyerang server orang lain tanpa izin.</li>
  <li>✅ Gunakan hanya untuk edukasi dan sistem milik sendiri.</li>
</ul>

<h2>👨‍💻 Developer</h2>
<ul>
  <li>Nama: X</li>
  <li>Versi: 4.0</li>
  <li>Tujuan: Edukasi Keamanan dan Etika Hacking</li>
</ul>

<script>
function copyCode(button) {
  const code = button.nextElementSibling.innerText;
  navigator.clipboard.writeText(code).then(() => {
    button.innerText = "✅ Disalin!";
    setTimeout(() => { button.innerText = "Salin"; }, 1500);
  });
}
</script>

</body>
</html>
