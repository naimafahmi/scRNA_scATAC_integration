export interface ExampleType {
    id: number;
    name: string;
    description?: string;
}

export type ExampleList = ExampleType[];

export interface ComponentProps {
    title: string;
    onClick: () => void;
}