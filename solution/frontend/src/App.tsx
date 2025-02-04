import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Header from "./components/Header"
import ProcessList from './components/ProcessList';
import FileUpload from './components/Upload';


export default function App() {
  

  return  (
    <Router>
      <Header/>
      <div className="p-4 bg-gray-100 min-h-screen">
        <h1 className="text-4xl text-center mb-8">News Scraping CAN</h1>

        {/* Enlaces de navegación */}
        <div className="mb-6 text-center">
          <Link to="/process-list" className="text-blue-400 mr-4">
            Ver Lista de Procesos
          </Link>
          <Link to="/file-upload" className="text-blue-500">
            Subir Archivo
          </Link>
        </div>

        {/* Rutas */}
        <Routes>
          <Route path="/process-list" element={<ProcessList />} />
          <Route path="/file-upload" element={<FileUpload />} />
        </Routes>
      </div>
    </Router>
  );
}