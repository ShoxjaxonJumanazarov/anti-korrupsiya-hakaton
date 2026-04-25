import networkx as nx
from typing import List, Dict


class CorruptionGraphAnalyzer:
    def __init__(self):
        self.G = nx.DiGraph()

    def add_employee(self, id: str, name: str, corruption_risk: float):
        """Xodim qo'shish"""
        self.G.add_node(id, name=name, risk=corruption_risk)

    def add_connection(self, from_id: str, to_id: str, connection_type: str):
        """Bog'liqlik qo'shish (mentor, tasdiqlovchi, hamkasb)"""
        self.G.add_edge(from_id, to_id, type=connection_type)

    def find_super_spreaders(self, top_n: int = 3) -> List[Dict]:
        """
        "Super tarqatuvchi"ni topish - eng ko'p bog'liqligi bo'lgan
        va yuqori riskli xodimlar
        """
        scores = {}

        for node in self.G.nodes():
            out_degree = self.G.out_degree(node)
            risk = self.G.nodes[node].get('risk', 0)
            scores[node] = out_degree * risk

        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        result = []
        for node_id, score in sorted_scores[:top_n]:
            result.append({
                'id': node_id,
                'name': self.G.nodes[node_id]['name'],
                'risk': self.G.nodes[node_id]['risk'],
                'connections': self.G.out_degree(node_id),
                'infection_score': round(score, 2)
            })

        return result

    def get_quarantine_list(self, super_spreader_id: str) -> List[Dict]:
        """
        Super tarqatuvchiga yaqin bo'lganlarni "karantin" ro'yxatiga olish
        """
        contacts = []
        for successor in self.G.successors(super_spreader_id):
            contacts.append({
                'id': successor,
                'name': self.G.nodes[successor]['name'],
                'connection_type': self.G[super_spreader_id][successor]['type'],
                'current_risk': self.G.nodes[successor].get('risk', 0)
            })
        return contacts


# ===== SINOV =====
if __name__ == "__main__":
    analyzer = CorruptionGraphAnalyzer()

    employees = [
        ("A1", "Karimov A.", 0.9),
        ("A2", "Nazarov B.", 0.3),
        ("A3", "Rahimov C.", 0.4),
        ("A4", "Saidov D.", 0.2),
        ("A5", "Hoshimov E.", 0.5),
    ]

    for emp in employees:
        analyzer.add_employee(*emp)

    connections = [
        ("A1", "A2", "mentor"),
        ("A1", "A3", "mentor"),
        ("A1", "A4", "tasdiqlovchi"),
        ("A1", "A5", "hamkasb"),
    ]

    for conn in connections:
        analyzer.add_connection(*conn)

    print("🔴 SUPER TARQATUVCHILAR:")
    spreaders = analyzer.find_super_spreaders()
    for sp in spreaders:
        print(f"  {sp['name']}: Infection Score = {sp['infection_score']}")
        print(f"    Bog'liqliklar: {sp['connections']}, Risk: {sp['risk']}")

    print("\n🏥 KARANTIN RO'YXATI (A1 uchun):")
    quarantine = analyzer.get_quarantine_list("A1")
    for q in quarantine:
        print(f"  {q['name']} - {q['connection_type']}")
