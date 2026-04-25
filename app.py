# Yechim Arxitekturasi

## Umumiy ko'rinish

```
[Foydalanuvchi (Fuqaro/Amaldor)]
        |
        v
[Web / Mobile App]  ←→  [FastAPI Backend]  ←→  [Neo4j Graph DB]
                                |
                         [NetworkX AI Engine]
                                |
                    [Super-Spreader Detection]
                                |
                       [Quarantine Manager]
```

## Komponentlar

### 1. Frontend (D3.js + HTML)
- Interaktiv tarmoq grafi
- Real-vaqtda yangilanish
- Super tarqatuvchini pulsatsiya bilan ko'rsatish
- Karantin va vaksina interfeysi

### 2. Backend (FastAPI)
- REST API endpointlari
- CORS qo'llab-quvvatlash
- Demo ma'lumotlarni avtomatik yuklash

### 3. Graph Analyzer (NetworkX)
- Out-degree hisoblash
- Risk * bog'liqlik = Infection Score
- "Super tarqatuvchi" identifikatsiyasi
- Karantin ro'yxatini shakllantirish

### 4. Ma'lumotlar bazasi (Neo4j)
- Graf ma'lumotlar bazasi
- Tugunlar: Xodimlar
- Qirralar: Bog'liqlik turlari

## API Endpointlari

| Method | URL | Tavsif |
|--------|-----|--------|
| GET | `/` | Holat tekshirish |
| POST | `/employees` | Xodim qo'shish |
| POST | `/connections` | Bog'liqlik qo'shish |
| GET | `/super-spreaders` | Top tarqatuvchilar |
| GET | `/quarantine/{id}` | Karantin ro'yxati |
| GET | `/graph` | Butun graf |
