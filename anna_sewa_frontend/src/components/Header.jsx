export default function Header() {
  return (
    <header style={{ padding: "1rem", borderBottom: "1px solid #ccc" }}>
      {/* Project Title + Nav placeholder */}
      <h1>AnnaSewa</h1>
      <nav>
        <a href="/">Home</a> | <a href="/about">About</a> | <a href="/features">Features</a>
      </nav>
    </header>
  );
}

