import { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [generatedSql, setGeneratedSql] = useState("");
  const [results, setResults] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!query.trim()) return;

    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: query,
        }),
      });

      const data = await response.json();

      setGeneratedSql(data.generated_sql);
      setResults(data.results);
    } catch (error) {
      console.error(error);
      alert("Failed to connect to backend.");
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white p-8 flex items-center justify-center">
      <div className="w-full max-w-4xl bg-slate-900 rounded-3xl shadow-2xl p-8 border border-slate-800">
        <h1 className="text-3xl font-bold mb-2">Text-to-SQL Semantic Parser</h1>
        <p className="text-slate-400 mb-6">Natural language to SQL demo interface</p>

        <textarea
          className="w-full h-32 rounded-2xl bg-slate-800 border border-slate-700 p-4 text-white outline-none"
          placeholder="Ask a question like: Show all users from USA"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />

        <button
          onClick={handleGenerate}
          className="mt-4 px-6 py-3 rounded-2xl bg-blue-600 hover:bg-blue-500 font-medium transition"
        >
          {loading ? "Generating..." : "Generate SQL"}
        </button>

        <div className="grid md:grid-cols-2 gap-6 mt-8">
          <div className="bg-slate-800 rounded-2xl p-4 border border-slate-700">
            <h2 className="font-semibold mb-3">Generated SQL</h2>
            <pre className="text-sm text-green-400 whitespace-pre-wrap">
              {generatedSql || "Generated SQL will appear here"}
            </pre>
          </div>

          <div className="bg-slate-800 rounded-2xl p-4 border border-slate-700">
            <h2 className="font-semibold mb-3">Results</h2>
            <pre className="text-sm text-slate-300 whitespace-pre-wrap">
              {results.length ? JSON.stringify(results, null, 2) : "Results will appear here"}
            </pre>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;