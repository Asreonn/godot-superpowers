# 02 - Godot 4.x Requirements: New Skills and Migration Needs

## Godot 4.x İçin Gerekli Yeni Skills

### Araştırma Özeti
Godot 4.x dokümantasyonu ve best practices incelendi. Mevcut 14 skill (3 orchestrator + 11 mini-skill) temel refactoring'i kapsıyor, ancak Godot 4.x'in yeni özellikleri için genişletilmesi gerekiyor.

---

## 1. GDScript 2.0 Modernizasyon Skills

### `godot-modernize-gdscript`
**Amaç:** GDScript 1.0 (Godot 3.x) pattern'lerini GDScript 2.0'a dönüştür

**Yapılacaklar:**
- [ ] `yield` → `await` dönüşümü
  - Detection: `yield(get_tree().create_timer(1.0), "timeout")`
  - Replacement: `await get_tree().create_timer(1.0).timeout`
  
- [ ] `onready` → `@onready` dönüşümü
  - Detection: `onready var player = $Player`
  - Replacement: `@onready var player: Node = $Player`
  
- [ ] Static typing ekleme
  - Detection: `var health = 100`
  - Replacement: `var health: int = 100`
  
- [ ] `export` → `@export` dönüşümü
  - Detection: `export var speed = 200`
  - Replacement: `@export var speed: float = 200.0`
  
- [ ] `setget` → property syntax dönüşümü
  - Detection: `var health setget set_health, get_health`
  - Replacement: Modern property syntax

**Örnek Input:**
```gdscript
# Eski GDScript 1.0
onready var player = $Player
export var speed = 200
func _ready():
    yield(get_tree().create_timer(1.0), "timeout")
```

**Örnek Output:**
```gdscript
# Modern GDScript 2.0
@onready var player: CharacterBody2D = $Player
@export var speed: float = 200.0
func _ready():
    await get_tree().create_timer(1.0).timeout
```

---

## 2. TileMap V2 (Godot 4.3+) Skills

### `godot-migrate-tilemap`
**Amaç:** Eski TileMap API'sini yeni TileMapLayer sistemine taşı

**Yapılacaklar:**
- [ ] TileMap node detection ve analiz
- [ ] `set_cell()` → `set_cells_terrain_connect()` migrasyonu
- [ ] TileSet resource conversion
- [ ] Physics layer mapping
- [ ] Navigation layer conversion
- [ ] Custom data layer preservation

**Detection Patterns:**
```bash
grep -rn "TileMap" --include="*.tscn" .
grep -rn "set_cell\|get_cell" --include="*.gd" .
grep -rn "tile_set" --include="*.gd" .
```

**Breaking Changes Coverage:**
- [ ] TileMap → TileMapLayer node değişikliği
- [ ] Cell coordinates sistemi değişikliği
- [ ] TileSet atlas organization değişikliği

---

## 3. Navigation Sistemi Skills

### `godot-setup-navigation`
**Amaç:** Yeni NavigationServer API'si ile navigation mesh kurulumu

**Yapılacaklar:**
- [ ] NavigationRegion2D/3D scene generation
- [ ] NavigationPolygon generation from TileMap
- [ ] NavigationAgent configuration
- [ ] Obstacle avoidance setup
- [ ] Pathfinding integration patterns

**Skill Input:**
```yaml
scene_type: 2D  # veya 3D
tilemap_node: Ground
obstacles: ["Walls", "Buildings"]
agent_radius: 16.0
```

**Generated Output:**
```gdscript
# Navigation setup script
extends NavigationRegion2D

@export var navigation_polygon: NavigationPolygon
@onready var agent: NavigationAgent2D = $NavigationAgent2D

func _ready():
    NavigationServer2D.map_set_active(navigation_map, true)
```

---

## 4. Multiplayer / Networking Skills

### `godot-setup-multiplayer`
**Amaç:** Yeni multiplayer API (MultiplayerPeer, MultiplayerSynchronizer) kurulumu

**Yapılacaklar:**
- [ ] MultiplayerSpawner configuration
- [ ] MultiplayerSynchronizer setup
- [ ] RPC (Remote Procedure Call) annotations
- [ ] Authority pattern implementation
- [ ] Host/Client scene structure

**Modern Pattern:**
```gdscript
@rpc
func update_position(new_position: Vector2):
    position = new_position

@rpc("call_local")
func shoot():
    spawn_bullet()
```

**Eski vs Yeni:**
- Eski: `remote func`, `master`, `puppet`
- Yeni: `@rpc`, `@rpc("call_local")`, `@rpc("any_peer")`

---

## 5. Rendering & Shader Skills

### `godot-optimize-rendering`
**Amaç:** Godot 4.x rendering pipeline optimizasyonu

**Yapılacaklar:**
- [ ] Renderer selection (Forward+, Mobile, Compatibility)
- [ ] 2D batching optimization detection
- [ ] Occlusion culling setup (3D)
- [ ] LOD (Level of Detail) configuration
- [ ] Shader uniform batching

**Detection:**
```bash
# Batching issues
grep -rn "modulate.*=.*Color" --include="*.gd" .  # Farklı modulate = batch break

# Material duplication
grep -rn "material.*=.*Material.new()" --include="*.gd" .
```

### `godot-convert-shaders`
**Amaç:** Godot 3.x shader'ları Godot 4.x'e taşı

**Değişiklikler:**
- [ ] `SCREEN_TEXTURE` → `screen_texture` (uniform)
- [ ] `DEPTH_TEXTURE` → `depth_texture` (uniform)
- [ ] `texture()` fonksiyon değişiklikleri
- [ ] Built-in varyings değişiklikleri
- [ ] Light function signature değişiklikleri

---

## 6. C# Integration Skills

### `godot-setup-csharp`
**Amaç:** C# script'leri Godot 4.x (.NET 6/8) ile entegrasyon

**Yapılacaklar:**
- [ ] C# project structure generation
- [ ] GDScript ↔ C# communication patterns
- [ ] Signal connection in C#
- [ ] Resource loading in C#
- [ ] Performance-critical code identification

**Pattern:**
```csharp
public partial class Player : CharacterBody2D
{
    [Export] public float Speed { get; set; } = 200.0f;
    
    public override void _Ready()
    {
        var sprite = GetNode<Sprite2D>("Sprite2D");
    }
}
```

---

## 7. Animation & State Machine Skills

### `godot-setup-animationtree`
**Amaç:** AnimationTree state machine kurulumu ve optimizasyonu

**Yapılacaklar:**
- [ ] AnimationTree node structure
- [ ] AnimationNodeStateMachine setup
- [ ] BlendSpace2D configuration
- [ ] State transition conditions
- [ ] Animation playback blending

**Input:**
```yaml
animation_player: "AnimationPlayer"
states: ["idle", "walk", "run", "attack"]
blend_parameters: ["velocity", "direction"]
```

---

## 8. Input & Action System Skills

### `godot-modernize-input`
**Amaç:** Input handling modernizasyonu

**Yapılacaklar:**
- [ ] `is_action_pressed()` → `Input.is_action_pressed()` (statik)
- [ ] Joypad rumble setup (Godot 4.x)
- [ ] Gyroscope/accelerometer input
- [ ] Input Map generation from code
- [ ] Context-sensitive input handling

---

## 9. Audio System Skills

### `godot-setup-audio-buses`
**Amaç:** Audio bus architecture kurulumu

**Yapılacaklar:**
- [ ] Master/Music/SFX bus structure
- [ ] AudioStreamPlayer pooling
- [ ] 3D audio spatial setup
- [ ] Audio effect chains (reverb, EQ)
- [ ] Music crossfade implementation

---

## 10. UI / Control Skills

### `godot-modernize-ui`
**Amaç:** UI sistemini Godot 4.x best practices'e taşı

**Yapılacaklar:**
- [ ] Theme resource extraction
- [ ] Control anchoring standardization
- [ ] UI scaling (hiDPI support)
- [ ] RichTextLabel BBCode patterns
- [ ] Custom control creation

**Patterns:**
```gdscript
# Theme usage
@export var button_theme: Theme
@onready var button: Button = $Button

func _ready():
    button.theme = button_theme
```

---

## 11. Performance Profiling Skills

### `godot-profile-performance`
**Amaç:** Performance bottleneck detection ve optimizasyon

**Yapılacaklar:**
- [ ] Profiler integration
- [ ] Frame time analysis
- [ ] Memory leak detection
- [ ] Draw call optimization
- [ ] Physics performance tuning

**Detection Commands:**
```bash
# Heavy _process functions
grep -rn "func _process" --include="*.gd" . | while read line; do
    file=$(echo $line | cut -d: -f1)
    line_num=$(echo $line | cut -d: -f2)
    echo "Checking $file:$line_num"
done

# get_node in loops
grep -rn "for.*in.*range.*:" --include="*.gd" -A5 . | grep "get_node"
```

---

## 12. Export & Platform Skills

### `godot-setup-export`
**Amaç:** Multi-platform export configuration

**Yapılacaklar:**
- [ ] Export preset generation (Windows, Mac, Linux, Web, Mobile)
- [ ] Icon and splash screen setup
- [ ] Feature tags configuration
- [ ] Custom build scripts
- [ ] CI/CD integration (GitHub Actions)

**Platforms:**
- [ ] Desktop (Windows, macOS, Linux)
- [ ] Web (HTML5/WebGL)
- [ ] Mobile (Android, iOS)
- [ ] Console (if available)

---

## 13. Testing Skills

### `godot-generate-tests`
**Amaç:** GUT (Godot Unit Test) veya custom test generation

**Yapılacaklar:**
- [ ] Test scene generation
- [ ] Unit test template creation
- [ ] Integration test patterns
- [ ] Mock/stub generation
- [ ] Test runner configuration

---

## 14. Plugin & Editor Extension Skills

### `godot-create-plugin`
**Amaç:** Godot Editor plugin skeleton generation

**Yapılacaklar:**
- [ ] plugin.cfg generation
- [ ] EditorPlugin script template
- [ ] Custom dock/panel creation
- [ ] Editor tool script patterns
- [ ] Plugin settings integration

---

## Skill Öncelik Matrisi

| Skill | Zorluk | Fayda | Öncelik | ETA |
|-------|--------|-------|---------|-----|
| godot-modernize-gdscript | Orta | Yüksek | P0 | 2 hafta |
| godot-migrate-tilemap | Yüksek | Yüksek | P0 | 3 hafta |
| godot-setup-navigation | Orta | Orta | P1 | 2 hafta |
| godot-setup-multiplayer | Yüksek | Orta | P1 | 3 hafta |
| godot-optimize-rendering | Orta | Yüksek | P1 | 2 hafta |
| godot-convert-shaders | Düşük | Orta | P2 | 1 hafta |
| godot-setup-csharp | Yüksek | Düşük | P2 | 3 hafta |
| godot-setup-animationtree | Orta | Orta | P1 | 2 hafta |
| godot-modernize-input | Düşük | Düşük | P3 | 1 hafta |
| godot-setup-audio-buses | Düşük | Orta | P2 | 1 hafta |
| godot-modernize-ui | Orta | Orta | P2 | 2 hafta |
| godot-profile-performance | Yüksek | Yüksek | P1 | 3 hafta |
| godot-setup-export | Orta | Orta | P2 | 2 hafta |
| godot-generate-tests | Orta | Yüksek | P1 | 2 hafta |
| godot-create-plugin | Düşük | Düşük | P3 | 1 hafta |

**Toplam: 15 yeni skill**
**Tahmini süre: 6-8 ay (paralel development)**

---

## Godot 4.x Özellik Özeti (Research Bulguları)

### 1. GDScript 2.0 Yenilikleri
- Static typing (`: int`, `: float`, `: Vector2`)
- `await` keyword (yield yerine)
- `@onready` decorator
- `@export` decorator
- Property syntax improvements
- `super()` method calls
- Typed arrays (`Array[int]`)

### 2. Rendering
- **Forward+**: High-end desktop
- **Mobile**: Mobile/integrated graphics
- **Compatibility**: OpenGL ES 3.0 (eski cihazlar)
- 2D batching improvements
- Occlusion culling (3D)
- SDFGI (Signed Distance Field Global Illumination)

### 3. TileMap V2 (Godot 4.3+)
- TileMapLayer nodes
- Terrain system
- Custom data layers
- Physics layers per tile
- Navigation layers
- Better TileSet editor

### 4. Navigation
- NavigationServer API
- NavigationRegion2D/3D
- NavigationAgent2D/3D
- Obstacle avoidance
- Runtime baking

### 5. Multiplayer
- MultiplayerPeer abstraction
- MultiplayerSpawner
- MultiplayerSynchronizer
- Scene replication
- RPC with `@rpc` annotation
- Authority system

### 6. Animation
- AnimationTree improvements
- BlendSpace2D/3D
- State machine transitions
- Animation retargeting
- Better bezier curves

---

## Implementasyon Roadmap

### Phase 1: Core Migration (Ay 1-2)
**Hedef:** En çok ihtiyaç duyulan 3 skill'i tamamla

1. **godot-modernize-gdscript** (P0)
   - Week 1-2: Detection patterns
   - Week 3-4: Replacement logic ve testing

2. **godot-migrate-tilemap** (P0)
   - Week 1-2: API research ve detection
   - Week 3-4: Migration logic ve test scenes
   - Week 5-6: Edge case handling

3. **godot-profile-performance** (P1)
   - Week 1-2: Detection patterns
   - Week 3-4: Optimization suggestions

### Phase 2: Advanced Features (Ay 3-4)
**Hedef:** Multiplayer ve navigation skills

4. **godot-setup-multiplayer**
5. **godot-setup-navigation**
6. **godot-optimize-rendering**

### Phase 3: Quality of Life (Ay 5-6)
**Hedef:** Developer experience improvements

7. **godot-generate-tests**
8. **godot-setup-export**
9. **godot-setup-animationtree**

### Phase 4: Niche Features (Ay 7-8)
**Hedef:** Spesifik kullanım alanları

10. Diğer P2/P3 skill'ler

---

## Başarı Kriterleri

### Her Skill İçin:
- [ ] Detection accuracy >90%
- [ ] False positive rate <5%
- [ ] Git commit per operation
- [ ] Rollback capability
- [ ] Godot 4.x project validation
- [ ] Dokümantasyon (SKILL.md + examples)

### Test Coverage:
- [ ] Unit tests for detection patterns
- [ ] Integration tests with sample projects
- [ ] Godot 4.0, 4.1, 4.2, 4.3 compatibility tests

---

## Eksik Tespit Edilen Alanlar

### Mevcut Skill'lerde Geliştirme:
1. **godot-refactor**: GDScript 2.0 specific patterns ekle
2. **godot-organize-project**: Godot 4.x folder structure önerileri güncelle
3. **godot-fix-positions**: Yeni node transform system desteği

### Dokümantasyon:
- Godot 4.x migration guide
- Renderer selection guide
- Platform-specific best practices

---

## Kaynaklar ve Referanslar

1. Godot 4.x Documentation: https://docs.godotengine.org/en/stable/
2. GDScript Reference: https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/
3. Best Practices: https://docs.godotengine.org/en/stable/tutorials/best_practices/
4. Migrating to Godot 4: https://docs.godotengine.org/en/stable/tutorials/migrating/
5. Godot 4.3 TileMap: https://docs.godotengine.org/en/stable/tutorials/2d/using_tilemaps/

---

## Sonraki Adımlar

1. **Bu hafta:**
   - [ ] godot-modernize-gdscript skill'i için planlama
   - [ ] Detection pattern'leri oluştur
   - [ ] Test projesi hazırla

2. **Gelecek ay:**
   - [ ] İlk 3 skill'i implemente et
   - [ ] Test coverage sağla
   - [ ] Dokümantasyon yaz

3. **Sürekli:**
   - [ ] Godot 4.x changelog'u takip et
   - [ ] Topluluk feedback'i topla
   - [ ] Yeni breaking changes için güncelleme

---

**Oluşturulma Tarihi:** 2026-02-02  
**Son Güncelleme:** 2026-02-02  
**Versiyon:** 1.0  
**Durum:** Planlama aşaması
