import { useState } from 'react'
import TruncatedText from './TruncatedText';

interface ProcessItem {
  id: number;
  user_id: number;
  timestamp: string;
  state: string;
  observation: string | null;
  date_scraping: string | null;
  title_scraping: string | null;
  content_scraping: string | null;
}

const ProcessList = () => {
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [clientId, setClientId] = useState<string>('');

  const [process, setProcess] = useState<ProcessItem[]>([]);

  const fetchProcess = async (clientId: string) => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(`http://localhost:9010/api/process/${clientId}`);
      if (!res.ok) {
        throw new Error('Error en la solicitud');
      }
      const data = await res.json();
      setProcess(data);
    } catch (error) {
      console.error("Error fetching process data:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    if (clientId.trim()) {
      fetchProcess(clientId);
    }
  };

  return (

    <div className="bg-gray-50 dark:bg-gray-700 dark:text-gray-400 text-black min-h-screen p-4 flex flex-col items-center">
      <form onSubmit={handleSubmit} className="mb-4">
        <input
          type="text"
          value={clientId}
          onChange={(e) => setClientId(e.target.value)}
          placeholder="Ingrese Client ID"
          className="px-4 py-2 rounded-lg border border-gray-300 mr-2"
        />
        <button type="submit" className="bg-blue-600 px-4 py-2 rounded-lg text-white">Buscar</button>
      </form>
      {loading && <p className="text-yellow-300">Cargando...</p>}
      {error && <p className="text-red-300">{error}</p>}


      <div className="overflow-x-auto p-4">
        <table className="w-full border border-gray-300 shadow-lg rounded-lg overflow-hidden">
          <thead className="bg-gray-200 text-gray-700">
            <tr>
              <th className="px-4 py-2 border">ID</th>
              <th className="px-4 py-2 border">User ID</th>
              <th className="px-4 py-2 border">Register Date</th>
              <th className="px-4 py-2 border">State</th>
              <th className="px-4 py-2 border">Observation</th>
              <th className="px-4 py-2 border">Content Scraping</th>

            </tr>
          </thead>
          <tbody>
            {process.map((item) => (
              <tr key={item.id} className="hover:bg-gray-100">
                <td className="px-4 py-2 border text-center">{item.id}</td>
                <td className="px-4 py-2 border text-center">{item.user_id}</td>
                <td className="px-4 py-2 border text-center">{item.timestamp}</td>
                <td
                  className={`px-4 py-2 border text-center font-semibold ${item.state === "Completado" ? "text-green-600" : "text-yellow-600"
                    }`}
                >
                  {item.state}
                </td>
                <td className="px-4 py-2 border text-center">{item.observation || ""}</td>
                <td className="px-4 py-2 border text-center">

                  {item.content_scraping != null ? (
                    <table>
                      <thead className="bg-gray-200 text-gray-700">
                        <tr>
                          <th className="px-4 py-2 border">News Date</th>
                          <th className="px-4 py-2 border">Title</th>
                          <th className="px-4 py-2 border">Content</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>{item.date_scraping}</td>
                          <td>{item.title_scraping}</td>
                          <td>
                            <TruncatedText text={item.content_scraping} maxLength={100} />
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  ) : (
                    <span>No content available</span> // O cualquier otro mensaje o elemento que quieras mostrar si no hay contenido
                  )}

                </td>

              </tr>
            ))}
          </tbody>
        </table>
      </div>

    </div >);
}

export default ProcessList;