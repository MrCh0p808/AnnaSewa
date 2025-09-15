import { useEffect, useState } from "react";
import { fetchHealth } from "../services/api";
import { log } from "../utils/logger";

export default function LandingPage() {
  const [health, setHealth] = useState({ status: "loading" });

  useEffect(() => {
    // Fetch backend /health on page load
    const loadHealth = async () => {
      const data = await fetchHealth();
      setHealth(data);
      log("Fetched /health", data);
    };
    loadHealth();
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Welcome to AnnaSewa</h2>
      <p>API Health Status: <strong>{health.status}</strong></p>
    </div>
  );
}

