import { useState } from 'react';
import axios from 'axios';

const FileUpload = () => {
  const [userId, setUserId] = useState<number>(0);
  const [file, setFile] = useState<File | null>(null);
  const [isUploading, setIsUploading] = useState<boolean>(false);
  const [uploadResponse, setUploadResponse] = useState<string | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file || userId <= 0) {
      alert('Por favor, selecciona un archivo y un ID de usuario');
      return;
    }

    setIsUploading(true);
    const formData = new FormData();
    formData.append('userId', userId.toString());
    formData.append('file', file);
    
    try {
      const response = await axios.post('http://localhost:9010/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log(response);
      setUploadResponse('Archivo cargado correctamente, se detecto (' + response.data.total_lines + ') links para scraper.');
    } catch (error) {
      setUploadResponse('Error al cargar el archivo');
      console.error(error);
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="p-4 bg-gray-100 min-h-screen flex justify-center">
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded shadow-md w-96">
        <h2 className="text-2xl font-semibold mb-4">Subir archivo</h2>
        <div className="mb-4">
          <label htmlFor="userId" className="block text-sm font-medium text-gray-700">
            User ID
          </label>
          <input
            type="text"
            id="userId"
            value={userId}
            onChange={(e) => setUserId(Number(e.target.value))}
            className="mt-1 p-2 border rounded w-full"
          />
        </div>

        <div className="mb-4">
          <label htmlFor="file" className="block text-sm font-medium text-gray-700">
            Archivo
          </label>
          <input
            type="file"
            id="file"
            onChange={handleFileChange}
            className="mt-1 p-2 border rounded w-full"
          />
        </div>

        <div className="flex justify-between items-center">
          <button
            type="submit"
            className="bg-blue-500 text-white px-4 py-2 rounded"
            disabled={isUploading}
          >
            {isUploading ? 'Subiendo...' : 'Subir'}
          </button>
        </div>

        {uploadResponse && (
          <div className="mt-4 text-center text-sm text-gray-700">
            {uploadResponse}
          </div>
        )}
      </form>
    </div>
  );
};

export default FileUpload;
