// src/data/sampleItems.ts
export interface Item {
  id: number;
  title: string;
  author: string;
  doc: string;
  description: string;
  image: string;      // large image shown in the main area
}

export const items: Item[] = [
  {
    id: 1,
    title: 'Sunset Over the Hills',
    author: 'Alice Johnson',
    description: 'A warm orange sunset casting long shadows over rolling hills.',
    doc: '/docs/sample-1.pdf', // added document field
    image: '/img/sample-1.png',
  },
  {
    id: 2,
    title: 'City Lights at Night',
    author: 'Bob Smith',
    description: 'Skyscrapers illuminated against a deep blue night sky.',
    doc: '/docs/sample-2.pdf', // added document field
    image: '/img/sample-2.png',
  },
  {
    id: 3,
    title: 'Misty Forest Path',
    author: 'Clara Lee',
    description: 'A quiet path winding through a mist‑filled forest.',
    doc: '/docs/sample-3.pdf', // added document field
    image: '/img/sample-3.png',
  },
  {
    id: 4,
    title: 'Sunset Over the Hills',
    author: 'Alice Johnson',
    description: 'A warm orange sunset casting long shadows over rolling hills.',
    doc: '/docs/sample-1.pdf', // added document field
    image: '/img/sample-1.png',
  },
  {
    id: 5,
    title: 'City Lights at Night',
    author: 'Bob Smith',
    description: 'Skyscrapers illuminated against a deep blue night sky.',
    doc: '/docs/sample-2.pdf', // added document field
    image: '/img/sample-2.png',
  },
  {
    id: 6,
    title: 'Misty Forest Path',
    author: 'Clara Lee',
    description: 'A quiet path winding through a mist‑filled forest.',
    doc: '/docs/sample-3.pdf', // added document field
    image: '/img/sample-3.png',
  },
];
