import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header style={{ padding: "1rem", backgroundColor: "#1E90FF", color: "#fff" }}>
      <h1>AnnaSewa</h1>
      <nav>
        {/* Navigation links */}
        <Link to="/" style={{ marginRight: "1rem", color: "#fff" }}>Home</Link>
        <Link to="/placeholder" style={{ color: "#fff" }}>Placeholder</Link>
      </nav>
    </header>
  );
}

