# 03 - Implementation Roadmap: Detailed Execution Plan

**Proje:** Godot Superpowers Skill Ekosistemi v3.0 → v4.0  
**Tarih:** 2026-02-02  
**Durum:** 🟡 Planlama Aşaması  
**Hedef:** Endüstri standardı Godot 4.x skill kütüphanesi

---

## 📚 Dokümantasyon Haritası

Bu repo 3 ana doküman içerir:

1. **[01_VISION_AND_STRATEGY.md](./01_VISION_AND_STRATEGY.md)** - Stratejik plan ve endüstri standartları
2. **[02_GODOT4_REQUIREMENTS.md](./02_GODOT4_REQUIREMENTS.md)** - Godot 4.x özellikleri ve yeni skill ihtiyaçları
3. **[03_IMPLEMENTATION_ROADMAP.md](./03_IMPLEMENTATION_ROADMAP.md)** - Bu dosya: Detaylı uygulama planı ve todo listesi

---

## 🎯 Uygulama Fazları

### Faz 0: Hazırlık ve Altyapı (Hafta 1-2)
**Hedef:** Çalışma ortamını hazırla, mevcut kodu analiz et

#### Todo Listesi:

**Hafta 1: Mevcut Durum Analizi**
- [x] Mevcut 14 skill'i listele ve kategorize et
- [x] Her skill'in SKILL.md frontmatter'ını analiz et
- [x] Eksik metadata alanlarını belirle (version, author, license vb.)
- [x] Mevcut dökümantasyonu incele (30+ dosya, 4600+ satır)
- [x] Test altyapısını değerlendir (mevcut: 0%)
- [x] Godot 4.x changelog'u oku (4.0 → 4.4)

**Hafta 2: Altyapı Kurulumu**
- [ ] GitHub repo yapılandırması (branch protection, PR templates)
- [ ] GitHub Actions CI/CD pipeline kurulumu
- [ ] Test framework seçimi (pytest/bash) ve kurulumu
- [ ] Skill validasyon script'i oluştur (SKILL.md format kontrolü)
- [ ] Örnek Godot 4.x test projeleri hazırla (2D, 3D, farklı sürümler)
- [ ] AGENTS.md şablonu oluştur

**Deliverables:**
- [ ] Çalışan CI/CD pipeline
- [ ] Test projeleri (en az 3 farklı Godot 4.x sürümü)
- [ ] Skill validasyon aracı
- [ ] Branch: `setup/infrastructure`

---

### Faz 1: Mevcut Skill'leri Modernize Et (Hafta 3-6)
**Hedef:** 14 mevcut skill'i endüstri standartlarına yükselt

#### 1.1 SKILL.md Frontmatter Güncelleme (Hafta 3-4)

**Her skill için (14 adet):**

**Orchestrators (3):**
- [ ] **godot-refactor/SKILL.md**
  - [ ] Add: `version: 3.0.0`
  - [ ] Add: `displayName: "Godot Refactoring Orchestrator"`
  - [ ] Add: `author`, `license: MIT`, `repository`
  - [ ] Add: `category: game-development`, `type: agent`
  - [ ] Add: `platforms: [macos, linux, windows]`
  - [ ] Add: `keywords: [godot, refactoring, code-quality]`
  - [ ] Add: `filesystem` permissions
  - [ ] Add: `behavior.timeout: 600`
  
- [ ] **godot-organize-project/SKILL.md**
  - [ ] Tüm frontmatter alanlarını güncelle
  - [ ] Permission tanımları ekle
  
- [ ] **godot-fix-positions/SKILL.md**
  - [ ] Tüm frontmatter alanlarını güncelle
  - [ ] Permission tanımları ekle

**Mini-Skills (11):**
- [ ] **godot-extract-to-scenes/SKILL.md** - Frontmatter güncelle
- [ ] **godot-split-scripts/SKILL.md** - Frontmatter güncelle
- [ ] **godot-add-signals/SKILL.md** - Frontmatter güncelle
- [ ] **godot-extract-resources/SKILL.md** - Frontmatter güncelle
- [ ] **godot-clean-conflicts/SKILL.md** - Frontmatter güncelle
- [ ] **godot-organize-files/SKILL.md** - Frontmatter güncelle
- [ ] **godot-organize-assets/SKILL.md** - Frontmatter güncelle
- [ ] **godot-organize-scripts/SKILL.md** - Frontmatter güncelle
- [ ] **godot-sync-static-positions/SKILL.md** - Frontmatter güncelle
- [ ] **godot-sync-camera-positions/SKILL.md** - Frontmatter güncelle
- [ ] **godot-sync-parallax/SKILL.md** - Frontmatter güncelle

**Validation:**
- [ ] Tüm skill'ler SKILL.md v2.0 spec'e uygun mu?
- [ ] Validasyon script'i tümünü geçiyor mu?
- [ ] GitHub Actions başarılı mı?

**Deliverables:**
- [ ] 14 güncellenmiş SKILL.md
- [ ] Validasyon raporu
- [ ] Branch: `update/frontmatter`

---

#### 1.2 Güvenlik ve İzin Sistemi (Hafta 5)

**Her skill için filesystem permissions:**

```yaml
# Örnek permission yapısı (godot-refactor için)
filesystem:
  read:
    - "${PROJECT_ROOT}/**/*.gd"
    - "${PROJECT_ROOT}/**/*.tscn"
    - "${PROJECT_ROOT}/project.godot"
    - "${PROJECT_ROOT}/**/*.tres"
  write:
    - "${PROJECT_ROOT}/**/*.gd"
    - "${PROJECT_ROOT}/**/*.tscn"
    - "${PROJECT_ROOT}/components/**"
    - "${PROJECT_ROOT}/resources/**"
  deny:
    - "**/.env*"
    - "**/secrets*"
    - "**/*.key"
    - "**/*.pem"
```

**Yapılacaklar:**
- [ ] Her skill için minimum gerekli permission'ları belirle
- [ ] Dangerous operation detection kuralları yaz
- [ ] Pre-execution safety checks implemente et
- [ ] Rollback capability için git hook'ları hazırla

**Deliverables:**
- [ ] 14 skill için permission tanımları
- [ ] Güvenlik dokümantasyonu (SECURITY.md)
- [ ] Branch: `feature/security-permissions`

---

#### 1.3 Test Altyapısı (Hafta 6)

**Unit Test Yapısı:**
```python
# Örnek test yapısı (test_godot_refactor.py)
def test_extract_to_scenes_detection():
    """Test .new() pattern detection"""
    code = "var timer = Timer.new()"
    result = detect_code_created_objects(code)
    assert result.found == True
    assert result.node_type == "Timer"
```

**Yapılacaklar:**
- [ ] Detection pattern'leri için unit test'ler yaz
- [ ] Integration test'ler oluştur (gerçek Godot projeleriyle)
- [ ] Test coverage raporu (hedef: >80%)
- [ ] GitHub Actions test pipeline'ı güncelle
- [ ] Test dokümantasyonu yaz

**Test Scenarios:**
- [ ] Basit Godot 4.0 projesi (2D platformer)
- [ ] Karmaşık Godot 4.2 projesi (3D RPG)
- [ ] Godot 3.x → 4.x migration projesi
- [ ] Hatalı/bozuk kod içeren proje (edge cases)

**Deliverables:**
- [ ] Test suite (50+ test case)
- [ ] Test coverage raporu
- [ ] CI/CD test pipeline
- [ ] Branch: `feature/testing-infrastructure`

---

### Faz 2: Godot 4.x Yeni Skill'leri (Hafta 7-18)
**Hedef:** 15 yeni skill implemente et (öncelik sırasına göre)

#### Sprint 1: Core GDScript 2.0 (Hafta 7-9)
**Skill:** `godot-modernize-gdscript`
**Öncelik:** P0 (Kritik)
**Zorluk:** Orta

**Hafta 7: Detection Patterns**
- [ ] `yield(...)` pattern detection yaz
  ```bash
  grep -rn "yield(" --include="*.gd" .
  grep -rn "yield.*get_tree()" --include="*.gd" .
  ```
- [ ] `onready var` detection yaz
- [ ] `export var` detection yaz
- [ ] `setget` property detection yaz
- [ ] Test: 10 farklı kod örneğiyle validation

**Hafta 8: Replacement Logic**
- [ ] `yield` → `await` dönüşüm implementasyonu
  ```gdscript
  # Input
  yield(get_tree().create_timer(1.0), "timeout")
  # Output
  await get_tree().create_timer(1.0).timeout
  ```
- [ ] `onready` → `@onready` dönüşümü
- [ ] Type inference mantığı (var → : Type)
- [ ] `setget` → modern property syntax
- [ ] Git commit per file mantığı

**Hafta 9: Testing & Dokümantasyon**
- [ ] Unit test'ler yaz (20+ test case)
- [ ] Integration test: Gerçek Godot 3.x projesi
- [ ] SKILL.md yaz (detaylı frontmatter)
- [ ] Examples.md oluştur (before/after)
- [ ] README.md güncelle

**Deliverables:**
- [ ] Çalışan `godot-modernize-gdscript` skill
- [ ] Test coverage >90%
- [ ] Tam dokümantasyon
- [ ] Branch: `feature/gdscript-modernize`

---

#### Sprint 2: TileMap Migration (Hafta 10-13)
**Skill:** `godot-migrate-tilemap`
**Öncelik:** P0 (Kritik)
**Zorluk:** Yüksek

**Hafta 10: API Research & Detection**
- [ ] Godot 4.3 TileMap API'sini detaylı incele
- [ ] Eski `set_cell()` vs yeni `set_cells_terrain_connect()` karşılaştır
- [ ] Detection patterns yaz:
  ```bash
  grep -rn "TileMap" --include="*.tscn" .
  grep -rn "set_cell\|get_cell" --include="*.gd" .
  grep -rn "tile_set" --include="*.gd" .
  grep -rn "update_bitmask_area" --include="*.gd" .
  ```
- [ ] Breaking changes listesi oluştur

**Hafta 11: Migration Logic**
- [ ] TileMap node analiz fonksiyonu
- [ ] TileSet resource conversion mantığı
- [ ] Physics layer mapping
- [ ] Navigation layer conversion
- [ ] Custom data layer preservation

**Hafta 12: Scene Generation**
- [ ] TileMapLayer node'ları oluştur
- [ ] Terrain sistemi kurulumu
- [ ] Atlas organization dönüşümü
- [ ] Cell coordinates dönüşümü

**Hafta 13: Testing & Dokümantasyon**
- [ ] Test projesi: Godot 3.x TileMap projesi
- [ ] Migration sonrası validation
- [ ] Edge case'leri test et (custom tile data, vb.)
- [ ] Tam dokümantasyon

**Deliverables:**
- [ ] Çalışan `godot-migrate-tilemap` skill
- [ ] Test coverage >85%
- [ ] Migration guide dokümantasyonu
- [ ] Branch: `feature/tilemap-migration`

---

#### Sprint 3: Performance & Testing (Hafta 14-16)
**Skill'ler:** `godot-profile-performance` + `godot-generate-tests`
**Öncelik:** P1 (Önemli)
**Zorluk:** Orta-Yüksek

**Hafta 14-15: Performance Profiling**
- [ ] Godot Profiler integration mantığı
- [ ] Detection patterns:
  ```bash
  # Heavy _process functions
  grep -rn "func _process" --include="*.gd" . | wc -l
  
  # get_node in loops
  grep -rn "for.*in.*range.*:" --include="*.gd" -A5 . | grep "get_node"
  
  # Instantiating in _process
  grep -rn "func _process" --include="*.gd" -A10 . | grep "\.new()\|instantiate()"
  ```
- [ ] Frame time analysis mantığı
- [ ] Memory leak detection patterns
- [ ] Draw call optimization önerileri
- [ ] Physics performance tuning suggestions

**Hafta 16: Test Generation**
- [ ] GUT (Godot Unit Test) integration
- [ ] Test template generation mantığı
- [ ] Mock/stub creation patterns
- [ ] Integration test örnekleri
- [ ] Test runner configuration

**Deliverables:**
- [ ] `godot-profile-performance` skill
- [ ] `godot-generate-tests` skill
- [ ] Test coverage >80%
- [ ] Branch: `feature/performance-testing`

---

#### Sprint 4: Navigation & Multiplayer (Hafta 17-20)
**Skill'ler:** `godot-setup-navigation` + `godot-setup-multiplayer`
**Öncelik:** P1 (Önemli)
**Zorluk:** Yüksek

**Hafta 17-18: Navigation Setup**
- [ ] NavigationServer API entegrasyonu
- [ ] NavigationRegion2D/3D scene generation
- [ ] NavigationPolygon generation from TileMap
- [ ] NavigationAgent configuration
- [ ] Obstacle avoidance setup
- [ ] Pathfinding integration patterns

**Hafta 19-20: Multiplayer Setup**
- [ ] MultiplayerPeer abstraction kurulumu
- [ ] MultiplayerSpawner configuration
- [ ] MultiplayerSynchronizer setup
- [ ] RPC annotation patterns:
  ```gdscript
  @rpc
  func update_position(new_position: Vector2):
      position = new_position
  
  @rpc("call_local")
  func shoot():
      spawn_bullet()
  ```
- [ ] Host/Client scene structure generation
- [ ] Authority pattern implementation

**Deliverables:**
- [ ] `godot-setup-navigation` skill
- [ ] `godot-setup-multiplayer` skill
- [ ] Örnek projeler (2D navigation, multiplayer lobby)
- [ ] Branch: `feature/navigation-multiplayer`

---

### Faz 3: İleri Seviye Skill'ler (Hafta 21-30)
**Hedef:** Kalan 11 skill'i implemente et

#### Sprint 5: Rendering & Shaders (Hafta 21-23)
- [ ] `godot-optimize-rendering`
  - [ ] Renderer selection (Forward+, Mobile, Compatibility)
  - [ ] 2D batching optimization
  - [ ] Occlusion culling setup
  - [ ] LOD configuration
  
- [ ] `godot-convert-shaders`
  - [ ] `SCREEN_TEXTURE` → `screen_texture`
  - [ ] Shader syntax değişiklikleri
  - [ ] Built-in varyings güncelleme

#### Sprint 6: C# & UI (Hafta 24-26)
- [ ] `godot-setup-csharp`
  - [ ] C# project structure
  - [ ] GDScript ↔ C# communication
  - [ ] Signal connection in C#
  
- [ ] `godot-modernize-ui`
  - [ ] Theme resource extraction
  - [ ] UI scaling (hiDPI)
  - [ ] Custom control creation

#### Sprint 7: Audio & Animation (Hafta 27-28)
- [ ] `godot-setup-audio-buses`
  - [ ] Master/Music/SFX bus structure
  - [ ] AudioStreamPlayer pooling
  - [ ] 3D spatial audio setup
  
- [ ] `godot-setup-animationtree`
  - [ ] AnimationTree state machine
  - [ ] BlendSpace2D/3D
  - [ ] State transition conditions

#### Sprint 8: Export & Input (Hafta 29-30)
- [ ] `godot-setup-export`
  - [ ] Multi-platform export presets
  - [ ] Icon/splash setup
  - [ ] CI/CD integration
  
- [ ] `godot-modernize-input`
  - [ ] Input Map generation
  - [ ] Joypad rumble setup
  - [ ] Context-sensitive input

**Deliverables:**
- [ ] 11 yeni skill
- [ ] Her biri için test coverage >80%
- [ ] Tam dokümantasyon
- [ ] Branch: `feature/advanced-skills`

---

### Faz 4: Godot 3.x Backward Compatibility (Hafta 31-34)
**Hedef:** Mevcut skill'leri Godot 3.x desteği ile güncelle

#### Hafta 31-32: Godot 3.x Detection
- [ ] Godot 3.x vs 4.x detection mantığı
- [ ] `.tscn` format=2 desteği
- [ ] GDScript 1.0 pattern recognition
- [ ] Versiyon-specific detection patterns

#### Hafta 33-34: Dual Mode Implementation
- [ ] Her skill için Godot 3.x ve 4.x desteği
- [ ] Auto-detection: Proje Godot 3 mü 4 mü?
- [ ] Conditional logic implementation
- [ ] Backward compatibility testing

**Deliverables:**
- [ ] Tüm skill'ler Godot 3.x + 4.x destekli
- [ ] Versiyon detection aracı
- [ ] Migration guide dokümantasyonu
- [ ] Branch: `feature/godot3-support`

---

### Faz 5: Dokümantasyon ve Topluluk (Hafta 35-38)
**Hedef:** Profesyonel dokümantasyon ve topluluk katkısı altyapısı

#### Hafta 35-36: Dokümantasyon
- [ ] Ana README.md güncelle
- [ ] CONTRIBUTING.md oluştur
- [ ] CODE_OF_CONDUCT.md oluştur
- [ ] CHANGELOG.md şablonu
- [ ] Video tutorial script'leri yaz
- [ ] API reference dokümantasyonu

#### Hafta 37-38: Topluluk Altyapısı
- [ ] Issue templates (bug report, feature request)
- [ ] Pull request template
- [ ] Skill template generator script
- [ ] Mini-skill development guide
- [ ] Topluluk showcase galerisi hazırla

**Deliverables:**
- [ ] Profesyonel dokümantasyon seti
- [ ] Topluluk katkı altyapısı
- [ ] GitHub repo tamamen hazır
- [ ] Branch: `docs/community-setup`

---

### Faz 6: Final Testing & Release (Hafta 39-40)
**Hedef:** v4.0.0 release için son hazırlıklar

#### Hafta 39: Final Testing
- [ ] End-to-end test: Tüm skill'ler bir projede test edilecek
- [ ] Performance test: 1000+ dosyalı projede test
- [ ] Cross-platform test: Windows, macOS, Linux
- [ ] Godot versiyon test: 4.0, 4.1, 4.2, 4.3, 4.4
- [ ] Security audit: Permission bypass test

#### Hafta 40: Release Preparation
- [ ] Versiyon tag: `v4.0.0`
- [ ] Release notes yaz
- [ ] GitHub release oluştur
- [ ] Installasyon script'lerini güncelle
- [ ] Topluluk duyurusu hazırla

**Deliverables:**
- [ ] 🎉 v4.0.0 Release!
- [ ] Tüm skill'ler production-ready
- [ ] Tam test coverage
- [ ] Profesyonel dokümantasyon

---

## 📊 İlerleme Takibi

### Her Faz İçin Metrikler:

| Faz | Skill Sayısı | Test Coverage | Dokümantasyon | ETA |
|-----|--------------|---------------|---------------|-----|
| Faz 0 | - | - | %50 | 2 hafta |
| Faz 1 | 14 | %80 | %70 | 4 hafta |
| Faz 2 | 4 | %85 | %80 | 8 hafta |
| Faz 3 | 11 | %80 | %80 | 10 hafta |
| Faz 4 | 14+ | %85 | %90 | 4 hafta |
| Faz 5 | - | - | %100 | 4 hafta |
| Faz 6 | 29 | %90 | %100 | 2 hafta |

**Toplam: 34 hafta (~8 ay)**

---

## 🎯 Hedeflenen Son Durum (v4.0.0)

### Skill Sayıları:
- **Orchestrators:** 3 (mevcut)
- **Mini-Skills:** 11 (mevcut) + 15 (yeni) = 26
- **Toplam:** 29 skill

### Kalite Metrikleri:
- **Test Coverage:** >%90
- **Documentation:** %100
- **Godot Versiyon Desteği:** 3.5+ ve 4.0+
- **Platform Desteği:** Windows, macOS, Linux

### Özellikler:
- ✅ Endüstri standardı SKILL.md formatı
- ✅ Güvenlik permission sistemi
- ✅ CI/CD pipeline
- ✅ Comprehensive test coverage
- ✅ Godot 4.x yeni özellikler desteği
- ✅ Godot 3.x backward compatibility
- ✅ Profesyonel dokümantasyon
- ✅ Topluluk katkı altyapısı

---

## 🚀 Hemen Başlayabileceğin Görevler

### Bu Hafta (Faz 0 - Hafta 1):

**Görev 1: Mevcut Durum Analizi**
```bash
# Mevcut tüm skill'leri listele
find /home/asreonn/godot-superpowers -name "SKILL.md" | sort

# Her birinin satır sayısını kontrol et
find /home/asreonn/godot-superpowers -name "SKILL.md" -exec wc -l {} \;

# Frontmatter içerenleri kontrol et
grep -l "^---" /home/asreonn/godot-superpowers/*/SKILL.md
```

**Görev 2: GitHub Actions Kurulumu**
- [ ] `.github/workflows/` dizini oluştur
- [ ] `ci.yml` dosyası oluştur
- [ ] Skill validasyon adımı ekle
- [ ] Test çalıştırma adımı ekle

**Görev 3: İlk Test Projesi**
- [ ] `test-projects/` dizini oluştur
- [ ] Basit 2D platformer projesi (Godot 4.2)
- [ ] Basit 3D projesi (Godot 4.2)
- [ ] Godot 3.x projesi (migration test için)

---

## 📋 Aylık Todo Özetleri

### Ocak 2026 (Hafta 1-4)
- [x] İki ana dokümanı oluştur (MASTER_PLAN, GODOT4_REQUIREMENTS)
- [ ] Faz 0: Altyapı kurulumu tamamla
- [ ] Faz 1: İlk 3 skill'in frontmatter'ını güncelle

### Şubat 2026 (Hafta 5-8)
- [ ] Faz 1: Kalan 11 skill'in frontmatter'ını güncelle
- [ ] Faz 1: Güvenlik permission sistemi
- [ ] Sprint 1: godot-modernize-gdscript başla

### Mart 2026 (Hafta 9-12)
- [ ] Sprint 1: godot-modernize-gdscript tamamla
- [ ] Sprint 2: godot-migrate-tilemap başla

### Nisan 2026 (Hafta 13-16)
- [ ] Sprint 2: godot-migrate-tilemap tamamla
- [ ] Sprint 3: Performance & Testing skills

### Mayıs 2026 (Hafta 17-20)
- [ ] Sprint 4: Navigation & Multiplayer
- [ ] Faz 2 tamamlanma kontrolü

### Haziran 2026 (Hafta 21-24)
- [ ] Sprint 5: Rendering & Shaders
- [ ] Sprint 6: C# & UI başla

### Temmuz 2026 (Hafta 25-28)
- [ ] Sprint 6: C# & UI tamamla
- [ ] Sprint 7: Audio & Animation

### Ağustos 2026 (Hafta 29-32)
- [ ] Sprint 8: Export & Input
- [ ] Faz 3 tamamlanma kontrolü
- [ ] Faz 4: Godot 3.x desteği başla

### Eylül 2026 (Hafta 33-36)
- [ ] Faz 4: Godot 3.x desteği tamamla
- [ ] Faz 5: Dokümantasyon

### Ekim 2026 (Hafta 37-40)
- [ ] Faz 5: Topluluk altyapısı
- [ ] Faz 6: Final testing
- [ ] 🎉 v4.0.0 Release!

---

## 🔄 Güncelleme Sıklığı

- **Haftalık:** Todo listesi güncelleme
- **Aylık:** İlerleme raporu ve milestone review
- **Faz başı:** Detaylı plan review ve ayarlama
- **Release öncesi:** Final checklist ve quality gate

---

## 📞 Yardım ve Destek

Bu planla ilgili sorularınız veya önerileriniz için:
- GitHub Issues: github.com/asreonn/godot-superpowers/issues
- Discussions: github.com/asreonn/godot-superpowers/discussions

---

**Son Güncelleme:** 2026-02-02  
**Sonraki Review:** 2026-02-09  
**Versiyon:** 1.0  
**Durum:** ✅ Planlama tamamlandı, uygulamaya hazır

---

*Bu doküman canlı bir plan olarak düzenli güncellenecektir.*
