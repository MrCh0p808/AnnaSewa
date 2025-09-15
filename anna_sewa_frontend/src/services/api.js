import axios from "axios";

// Base URL for backend API
const API_BASE = import.meta.env.VITE_API_BASE || "http://127.0.0.1:8000";

// Fetch /health endpoint
export const fetchHealth = async () => {
  try {
    const response = await axios.get(`${API_BASE}/health`);
    return response.data;
  } catch (err) {
    console.error("Error fetching /health:", err);
    return { status: "error" };
  }
};

// Fetch /status endpoint
export const fetchStatus = async () => {
  try {
    const response = await axios.get(`${API_BASE}/status`);
    return response.data;
  } catch (err) {
    console.error("Error fetching /status:", err);
    return { api_version: "unknown", db_status: "unknown" };
  }
};

