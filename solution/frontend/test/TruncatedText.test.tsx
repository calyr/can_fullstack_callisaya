import { describe, test, expect} from 'vitest'
import { render, screen } from '@testing-library/react';
import TruncatedText from '../src/components/TruncatedText';
import React from 'react';

describe('TruncatedText Component', () => {
  test('muestra el texto completo si es menor que maxLength', () => {
    render(<TruncatedText text="Hola mundo" maxLength={20} />);
    expect(screen.getByText('Hola mundo')).toBeInTheDocument();
  });

  test('trunca el texto y agrega "..." si es mayor que maxLength', () => {
    render(<TruncatedText text="Este es un texto largo" maxLength={10} />);
    expect(screen.getByText('Este es un...')).toBeInTheDocument();
  });

  test('muestra cadena vacía si text es null', () => {
    render(<TruncatedText text={null} maxLength={10} />);
    expect(screen.queryByText('...')).not.toBeInTheDocument(); // No debería mostrar nada
  });
});