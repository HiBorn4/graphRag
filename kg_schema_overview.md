## Node Labels

- `GroupCompany`
- `InventoryLevel1`
- `InventoryLevel4`
- `InventoryLevel2`
- `InventoryLevel3`

## Relationship Types

- `HAS_AMOUNT`
- `HAS_SUB_INVENTORY`

## Relationship Patterns

- `GroupCompany` -[`HAS_AMOUNT`]-> `InventoryLevel4`
- `InventoryLevel1` -[`HAS_SUB_INVENTORY`]-> `InventoryLevel2`
- `InventoryLevel2` -[`HAS_SUB_INVENTORY`]-> `InventoryLevel3`
- `InventoryLevel2` -[`HAS_SUB_INVENTORY`]-> `InventoryLevel4`
- `InventoryLevel3` -[`HAS_SUB_INVENTORY`]-> `InventoryLevel4`

## All Nodes by Label

### GroupCompany
- AS
- Agri
- CE
- CONT SOUR
- CORP
- FES
- HO
- INTNL OPER
- MDS
- NON MRV
- Powerol
- SBU
- SOURCING
- SWARAJ
- Synergy
- TPDS
- TW

### InventoryLevel1
- Inventories

### InventoryLevel4
- Clg Stock - Construction W I P - B/s
- Clg Stock - Finished Goods - B/s
- Clg Stock - Mfg Component B/s
- Clg Stock - Raw Material-B/s
- Clg Stock - Wip - B/s
- Clg Stock In Transit - FG B/s
- Clg Stock In Transit - Rm - B/s
- Closing Stock- Gunny Bags
- Construction Work In Progress
- Food & Beverages
- G-Stock Materiali Ricoperti CBN
- In Transit - Stores & Spares
- Ind-AS  Inventories
- Inventorie Consumable Stores & Misc.
- Inventory Dies
- Inventory Machinery Spares-Imported
- Inventory Manufactured Tools
- Inventory Oils, Grease & Chemicals
- Inventory Packing Material
- Inventory Spares
- Inventory Spares- Manual Adj
- Inventory Stores- Manual Adj
- Inventory Tools
- Inventory Tools- Manual Adj
- Plant & Machinery Held For Sale
- Stock in trade
- Stock in transit - Stores & Spares
- Stock in transit - Tools
- Stock in transit - Traded goods
- WIP- Seed Potato Facility A/c

### InventoryLevel2
- Finished Goods
- Inventory Machinery Spares
- Other Inventory
- Raw Material & Mfg. Componets
- Stock in Trade
- Stores and Spares
- Tools
- Work-in-Progress

### InventoryLevel3
- Finished Goods
- Raw Material & Mfg. Componet
- Stock In Transit - Finised Goods
- Stock In Transit - Raw Material
- Stock In Transit - Traded Goods
- Stock in Trade

## All Relationships (excluding actual values)

- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Raw Material-B/s)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Raw Material-B/s)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Mfg Component B/s)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Mfg Component B/s)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock In Transit - Rm - B/s)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock In Transit - Rm - B/s)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Wip - B/s)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Wip - B/s)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Finished Goods - B/s)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Finished Goods - B/s)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Stock in trade)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Stock in trade)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Oils, Grease & Chemicals)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Oils, Grease & Chemicals)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventorie Consumable Stores & Misc.)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventorie Consumable Stores & Misc.)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Stores- Manual Adj)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Stores- Manual Adj)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Packing Material)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Packing Material)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Machinery Spares-Imported)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Machinery Spares-Imported)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares- Manual Adj)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares- Manual Adj)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Manufactured Tools)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Manufactured Tools)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools- Manual Adj)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools- Manual Adj)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Dies)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Dies)
- (GroupCompany: AS) -[HAS_AMOUNT]-> (InventoryLevel4: In Transit - Stores & Spares)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Raw Material-B/s)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Raw Material-B/s)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Mfg Component B/s)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Mfg Component B/s)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock In Transit - Rm - B/s)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock In Transit - Rm - B/s)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Wip - B/s)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Wip - B/s)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Finished Goods - B/s)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Finished Goods - B/s)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Stock in trade)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Stock in trade)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Oils, Grease & Chemicals)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Oils, Grease & Chemicals)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventorie Consumable Stores & Misc.)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventorie Consumable Stores & Misc.)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Stock in transit - Stores & Spares)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Stock in transit - Stores & Spares)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Stores- Manual Adj)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Stores- Manual Adj)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Packing Material)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Packing Material)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Machinery Spares-Imported)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Machinery Spares-Imported)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares- Manual Adj)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares- Manual Adj)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Manufactured Tools)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Manufactured Tools)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools- Manual Adj)
- (GroupCompany: FES) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools- Manual Adj)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Raw Material-B/s)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Raw Material-B/s)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Mfg Component B/s)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Mfg Component B/s)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock In Transit - Rm - B/s)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock In Transit - Rm - B/s)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Wip - B/s)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Wip - B/s)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Finished Goods - B/s)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Finished Goods - B/s)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Stock in trade)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Stock in trade)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Oils, Grease & Chemicals)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Oils, Grease & Chemicals)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventorie Consumable Stores & Misc.)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventorie Consumable Stores & Misc.)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Stores- Manual Adj)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Stores- Manual Adj)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Packing Material)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Packing Material)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Machinery Spares-Imported)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares- Manual Adj)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares- Manual Adj)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Manufactured Tools)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Manufactured Tools)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools- Manual Adj)
- (GroupCompany: SWARAJ) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools- Manual Adj)
- (GroupCompany: Powerol) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Raw Material-B/s)
- (GroupCompany: Powerol) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Raw Material-B/s)
- (GroupCompany: Powerol) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Mfg Component B/s)
- (GroupCompany: Powerol) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Mfg Component B/s)
- (GroupCompany: Powerol) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Finished Goods - B/s)
- (GroupCompany: Powerol) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Finished Goods - B/s)
- (GroupCompany: Powerol) -[HAS_AMOUNT]-> (InventoryLevel4: Stock in trade)
- (GroupCompany: Powerol) -[HAS_AMOUNT]-> (InventoryLevel4: Stock in trade)
- (GroupCompany: Powerol) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Oils, Grease & Chemicals)
- (GroupCompany: Powerol) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Stores- Manual Adj)
- (GroupCompany: SBU) -[HAS_AMOUNT]-> (InventoryLevel4: Inventorie Consumable Stores & Misc.)
- (GroupCompany: SBU) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Packing Material)
- (GroupCompany: SBU) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Packing Material)
- (GroupCompany: SBU) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares)
- (GroupCompany: SBU) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares)
- (GroupCompany: SBU) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares- Manual Adj)
- (GroupCompany: SBU) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares- Manual Adj)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Raw Material-B/s)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Raw Material-B/s)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Mfg Component B/s)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Wip - B/s)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Wip - B/s)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Finished Goods - B/s)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Clg Stock - Finished Goods - B/s)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Oils, Grease & Chemicals)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Oils, Grease & Chemicals)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventorie Consumable Stores & Misc.)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventorie Consumable Stores & Misc.)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Stores- Manual Adj)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Stores- Manual Adj)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Packing Material)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Packing Material)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Spares)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Machinery Spares-Imported)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Machinery Spares-Imported)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Manufactured Tools)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Manufactured Tools)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools- Manual Adj)
- (GroupCompany: TW) -[HAS_AMOUNT]-> (InventoryLevel4: Inventory Tools- Manual Adj)
- (InventoryLevel1: Inventories) -[HAS_SUB_INVENTORY]-> (InventoryLevel2: Finished Goods)
- (InventoryLevel1: Inventories) -[HAS_SUB_INVENTORY]-> (InventoryLevel2: Stores and Spares)
- (InventoryLevel1: Inventories) -[HAS_SUB_INVENTORY]-> (InventoryLevel2: Raw Material & Mfg. Componets)
- (InventoryLevel1: Inventories) -[HAS_SUB_INVENTORY]-> (InventoryLevel2: Other Inventory)
- (InventoryLevel1: Inventories) -[HAS_SUB_INVENTORY]-> (InventoryLevel2: Inventory Machinery Spares)
- (InventoryLevel1: Inventories) -[HAS_SUB_INVENTORY]-> (InventoryLevel2: Stock in Trade)
- (InventoryLevel1: Inventories) -[HAS_SUB_INVENTORY]-> (InventoryLevel2: Tools)
- (InventoryLevel1: Inventories) -[HAS_SUB_INVENTORY]-> (InventoryLevel2: Work-in-Progress)
- (InventoryLevel2: Finished Goods) -[HAS_SUB_INVENTORY]-> (InventoryLevel3: Finished Goods)
- (InventoryLevel2: Finished Goods) -[HAS_SUB_INVENTORY]-> (InventoryLevel3: Stock In Transit - Finised Goods)
- (InventoryLevel2: Stores and Spares) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Inventory Oils, Grease & Chemicals)
- (InventoryLevel2: Stores and Spares) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Inventorie Consumable Stores & Misc.)
- (InventoryLevel2: Stores and Spares) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Stock in transit - Stores & Spares)
- (InventoryLevel2: Stores and Spares) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Inventory Stores- Manual Adj)
- (InventoryLevel2: Stores and Spares) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Inventory Packing Material)
- (InventoryLevel2: Stores and Spares) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: G-Stock Materiali Ricoperti CBN)
- (InventoryLevel2: Raw Material & Mfg. Componets) -[HAS_SUB_INVENTORY]-> (InventoryLevel3: Raw Material & Mfg. Componet)
- (InventoryLevel2: Raw Material & Mfg. Componets) -[HAS_SUB_INVENTORY]-> (InventoryLevel3: Stock In Transit - Raw Material)
- (InventoryLevel2: Other Inventory) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Food & Beverages)
- (InventoryLevel2: Other Inventory) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Ind-AS  Inventories)
- (InventoryLevel2: Other Inventory) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Plant & Machinery Held For Sale)
- (InventoryLevel2: Inventory Machinery Spares) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Inventory Spares)
- (InventoryLevel2: Inventory Machinery Spares) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Inventory Machinery Spares-Imported)
- (InventoryLevel2: Inventory Machinery Spares) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Inventory Spares- Manual Adj)
- (InventoryLevel2: Inventory Machinery Spares) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Inventory Manufactured Tools)
- (InventoryLevel2: Inventory Machinery Spares) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: In Transit - Stores & Spares)
- (InventoryLevel2: Stock in Trade) -[HAS_SUB_INVENTORY]-> (InventoryLevel3: Stock In Transit - Traded Goods)
- (InventoryLevel2: Stock in Trade) -[HAS_SUB_INVENTORY]-> (InventoryLevel3: Stock in Trade)
- (InventoryLevel2: Tools) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Inventory Tools)
- (InventoryLevel2: Tools) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Inventory Manufactured Tools)
- (InventoryLevel2: Tools) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Inventory Tools- Manual Adj)
- (InventoryLevel2: Tools) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Inventory Dies)
- (InventoryLevel2: Tools) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Stock in transit - Tools)
- (InventoryLevel2: Work-in-Progress) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Clg Stock - Wip - B/s)
- (InventoryLevel2: Work-in-Progress) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: WIP- Seed Potato Facility A/c)
- (InventoryLevel2: Work-in-Progress) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Construction Work In Progress)
- (InventoryLevel2: Work-in-Progress) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Clg Stock - Construction W I P - B/s)
- (InventoryLevel3: Finished Goods) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Clg Stock - Finished Goods - B/s)
- (InventoryLevel3: Stock In Transit - Traded Goods) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Stock in transit - Traded goods)
- (InventoryLevel3: Stock in Trade) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Stock in trade)
- (InventoryLevel3: Raw Material & Mfg. Componet) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Clg Stock - Raw Material-B/s)
- (InventoryLevel3: Raw Material & Mfg. Componet) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Clg Stock - Mfg Component B/s)
- (InventoryLevel3: Raw Material & Mfg. Componet) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Closing Stock- Gunny Bags)
- (InventoryLevel3: Stock In Transit - Finised Goods) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Clg Stock In Transit - FG B/s)
- (InventoryLevel3: Stock In Transit - Raw Material) -[HAS_SUB_INVENTORY]-> (InventoryLevel4: Clg Stock In Transit - Rm - B/s)

## All GroupCompany Nodes

- AS
- Agri
- CE
- CONT SOUR
- CORP
- FES
- HO
- INTNL OPER
- MDS
- NON MRV
- Powerol
- SBU
- SOURCING
- SWARAJ
- Synergy
- TPDS
- TW


## Property Keys for Nodes and Relationships in HAS_AMOUNT

### Node Label: GroupCompany
- name

### Node Label: InventoryLevel4
- name

### Relationship Type: HAS_AMOUNT
- amount
- year
